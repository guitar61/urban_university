from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext

API_TOKEN = ''

bot = Bot(token=API_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

# Main menu reply keyboard with "Calculate", "Information", and "Buy" buttons
main_menu_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
button_calculate = KeyboardButton("Calculate")
button_info = KeyboardButton("Information")
button_buy = KeyboardButton("Buy")  # New "Buy" button
main_menu_keyboard.add(button_calculate, button_info, button_buy)

# Inline keyboard for products with callback data
product_menu_kb = InlineKeyboardMarkup()
product_buttons = [
    InlineKeyboardButton("Product 1", callback_data="product_buying"),
    InlineKeyboardButton("Product 2", callback_data="product_buying"),
    InlineKeyboardButton("Product 3", callback_data="product_buying"),
    InlineKeyboardButton("Product 4", callback_data="product_buying"),
]
product_menu_kb.add(*product_buttons)

# /start command handler to display the main menu with the reply keyboard
@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer(
        "Hello! Press 'Calculate' to calculate your calorie intake or 'Information' for help.",
        reply_markup=main_menu_keyboard
    )

# Handler for "Information" button to provide bot details
@dp.message_handler(text="Information")
async def info(message: types.Message):
    await message.answer("This bot helps you calculate your daily calorie intake and shop for products.")

# Handler for "Calculate" button to show the inline options (if calculation functionality is present)
@dp.message_handler(text="Calculate")
async def main_menu(message: types.Message):
    await message.answer("Select an option:", reply_markup=inline_calculate_kb)

# Handler for "Buy" button to display products and images
@dp.message_handler(text="Buy")
async def get_buying_list(message: types.Message):
    # Define a list of product details with image paths
    products = [
        {"name": "Product 1", "description": "Description for product 1", "price": 100, "image_path": "1.webp"},
        {"name": "Product 2", "description": "Description for product 2", "price": 200, "image_path": "2.webp"},
        {"name": "Product 3", "description": "Description for product 3", "price": 300, "image_path": "3.webp"},
        {"name": "Product 4", "description": "Description for product 4", "price": 400, "image_path": "4.webp"},
    ]

    # Loop through each product and send its details and image
    for product in products:
        with open(product["image_path"], 'rb') as img:
            await message.answer_photo(
                img,
                caption=f"Name: {product['name']} | Description: {product['description']} | Price: {product['price']}"
            )

    # Send the inline product menu after displaying all product details
    await message.answer("Select a product to purchase:", reply_markup=product_menu_kb)

# Callback handler for selecting a product
@dp.callback_query_handler(lambda call: call.data == "product_buying")
async def send_confirm_message(call: types.CallbackQuery):
    await call.message.answer("You have successfully purchased the product!")
    await call.answer()  # Finalize the callback to prevent the button from remaining active

# Additional handlers for "Calculate" functionality, if required
# Inline button handler for "Calculation formulas"
@dp.callback_query_handler(lambda call: call.data == "formulas")
async def get_formulas(call: types.CallbackQuery):
    formula_text = "10 x weight (kg) + 6.25 x height (cm) - 5 x age (years) + 5 (for men) / -161 (for women)"
    await call.message.answer(formula_text)
    await call.answer()

# Inline button handler for "Calculate calorie intake" to start the FSM and ask for age
@dp.callback_query_handler(lambda call: call.data == "calories")
async def set_age(call: types.CallbackQuery):
    await call.message.answer("Please enter your age:")
    await UserState.age.set()
    await call.answer()

# FSM states to collect age, height, and weight
class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()

# FSM handler to collect age and ask for height
@dp.message_handler(state=UserState.age)
async def set_growth(message: types.Message, state: FSMContext):
    await state.update_data(age=message.text)
    await message.answer("Please enter your height (in cm):")
    await UserState.growth.set()

# FSM handler to collect height and ask for weight
@dp.message_handler(state=UserState.growth)
async def set_weight(message: types.Message, state: FSMContext):
    await state.update_data(growth=message.text)
    await message.answer("Please enter your weight (in kg):")
    await UserState.weight.set()

# FSM handler to collect weight, calculate calories, and send the result
@dp.message_handler(state=UserState.weight)
async def send_calories(message: types.Message, state: FSMContext):
    await state.update_data(weight=message.text)
    data = await state.get_data()

    age = int(data['age'])
    height = int(data['growth'])
    weight = int(data['weight'])

    # Calculate daily calorie intake using Mifflin-St Jeor formula (for men)
    calorie_norm = 10 * weight + 6.25 * height - 5 * age + 5
    await message.answer(f"Your daily calorie intake should be: {calorie_norm:.2f} kcal.")
    await state.finish()

# Run the bot
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

