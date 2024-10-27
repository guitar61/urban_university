from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext

API_TOKEN = ''

bot = Bot(token=API_TOKEN)
storage = MemoryStorage()  # Memory storage for FSM
dp = Dispatcher(bot, storage=storage)

# Step 1: Create the main menu reply keyboard with "Calculate" and "Information"
main_menu_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
button_calculate = KeyboardButton(text="Calculate")
button_info = KeyboardButton(text="Information")
main_menu_keyboard.add(button_calculate)
main_menu_keyboard.add(button_info)

# Step 2: Create the inline keyboard with options "Calculate calorie intake" and "Calculation formulas"
inline_calculate_kb = InlineKeyboardMarkup()
button_calories = InlineKeyboardButton(text="Calculate calorie intake", callback_data="calories")
button_formulas = InlineKeyboardButton(text="Calculation formulas", callback_data="formulas")
inline_calculate_kb.add(button_calories, button_formulas)

# Step 3: Define states for FSM to collect user's age, height, and weight
class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()

# Step 4: /start command handler to display the main menu with the reply keyboard
@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer(
        "Hello! Press 'Calculate' to calculate your calorie intake or 'Information' for help.",
        reply_markup=main_menu_keyboard
    )

# Step 5: Handler for "Information" button to provide bot details
@dp.message_handler(text="Information")
async def info(message: types.Message):
    await message.answer("This bot helps you calculate your daily calorie intake based on your input.")

# Step 6: Handler for "Calculate" button to show the inline options
@dp.message_handler(text="Calculate")
async def main_menu(message: types.Message):
    await message.answer("Select an option:", reply_markup=inline_calculate_kb)

# Step 7: Inline button handler for "Calculation formulas"
@dp.callback_query_handler(lambda call: call.data == "formulas")
async def get_formulas(call: types.CallbackQuery):
    formula_text = "10 x weight (kg) + 6.25 x height (cm) - 5 x age (years) + 5 (for men) / -161 (for women)"
    await call.message.answer(formula_text)
    await call.answer()  # Finalize the callback to prevent the button from remaining active

# Step 8: Inline button handler for "Calculate calorie intake" to start the FSM and ask for age
@dp.callback_query_handler(lambda call: call.data == "calories")
async def set_age(call: types.CallbackQuery):
    await call.message.answer("Please enter your age:")
    await UserState.age.set()  # Set FSM state to age
    await call.answer()

# Step 9: FSM handler to collect age and ask for height
@dp.message_handler(state=UserState.age)
async def set_growth(message: types.Message, state: FSMContext):
    await state.update_data(age=message.text)  # Store age in FSM context
    await message.answer("Please enter your height (in cm):")
    await UserState.growth.set()  # Move to the next state (height)

# Step 10: FSM handler to collect height and ask for weight
@dp.message_handler(state=UserState.growth)
async def set_weight(message: types.Message, state: FSMContext):
    await state.update_data(growth=message.text)  # Store height in FSM context
    await message.answer("Please enter your weight (in kg):")
    await UserState.weight.set()  # Move to the next state (weight)

# Step 11: FSM handler to collect weight, calculate calories, and send the result
@dp.message_handler(state=UserState.weight)
async def send_calories(message: types.Message, state: FSMContext):
    await state.update_data(weight=message.text)  # Store weight in FSM context
    data = await state.get_data()  # Retrieve stored data

    # Extract age, height, and weight as integers
    age = int(data['age'])
    height = int(data['growth'])
    weight = int(data['weight'])

    # Calculate daily calorie intake using Mifflin-St Jeor formula (for men)
    calorie_norm = 10 * weight + 6.25 * height - 5 * age + 5
    await message.answer(f"Your daily calorie intake should be: {calorie_norm:.2f} kcal.")

    # Finish the FSM process, resetting the state
    await state.finish()

# Run the bot
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
