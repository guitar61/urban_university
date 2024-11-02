from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from crud_functions import initiate_db, get_all_products

API_TOKEN = ''

bot = Bot(token=API_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

# Initialize the database and populate products
initiate_db()

# Main menu reply keyboard
main_menu_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
button_calculate = KeyboardButton("Calculate")
button_info = KeyboardButton("Information")
button_buy = KeyboardButton("Buy")
main_menu_keyboard.add(button_calculate, button_info, button_buy)

# Inline keyboard for selecting a product to purchase
product_menu_kb = InlineKeyboardMarkup(row_width=2)
products = get_all_products()
product_buttons = [InlineKeyboardButton(product[1], callback_data=f"buy_{product[0]}") for product in products]
product_menu_kb.add(*product_buttons)


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer(
        "Hello! Press 'Calculate' to calculate your calorie intake or 'Information' for help.",
        reply_markup=main_menu_keyboard
    )


@dp.message_handler(text="Information")
async def info(message: types.Message):
    await message.answer("This bot helps you calculate your daily calorie intake and shop for products.")


@dp.message_handler(text="Buy")
async def get_buying_list(message: types.Message):
    products = get_all_products()
    for product in products:
        product_id, title, description, price = product
        image_path = f"{product_id}.webp"  # Assuming images are named 1.webp, 2.webp, etc.
        try:
            with open(image_path, 'rb') as img:
                await message.answer_photo(
                    img,
                    caption=f"Название: {title} | Описание: {description} | Цена: {price}"
                )
        except FileNotFoundError:
            await message.answer(
                f"Название: {title} | Описание: {description} | Цена: {price}\n"
                f"Image not available."
            )

    await message.answer("Select a product to purchase:", reply_markup=product_menu_kb)


@dp.callback_query_handler(lambda call: call.data.startswith("buy_"))
async def send_confirm_message(call: types.CallbackQuery):
    product_id = call.data.split("_")[1]
    await call.message.answer(f"You have successfully purchased Product {product_id}!")
    await call.answer()


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


@dp.message_handler(text="Calculate")
async def calculate_options(message: types.Message):
    inline_calculate_kb = InlineKeyboardMarkup()
    button_calories = InlineKeyboardButton("Calculate calorie intake", callback_data="calories")
    button_formulas = InlineKeyboardButton("Calculation formulas", callback_data="formulas")
    inline_calculate_kb.add(button_calories, button_formulas)
    await message.answer("Select an option:", reply_markup=inline_calculate_kb)


@dp.callback_query_handler(lambda call: call.data == "formulas")
async def get_formulas(call: types.CallbackQuery):
    formula_text = "10 x weight (kg) + 6.25 x height (cm) - 5 x age (years) + 5 (for men) / -161 (for women)"
    await call.message.answer(formula_text)
    await call.answer()


@dp.callback_query_handler(lambda call: call.data == "calories")
async def set_age(call: types.CallbackQuery):
    await call.message.answer("Please enter your age:")
    await UserState.age.set()
    await call.answer()


@dp.message_handler(state=UserState.age)
async def set_growth(message: types.Message, state: FSMContext):
    await state.update_data(age=message.text)
    await message.answer("Please enter your height (in cm):")
    await UserState.growth.set()


@dp.message_handler(state=UserState.growth)
async def set_weight(message: types.Message, state: FSMContext):
    await state.update_data(growth=message.text)
    await message.answer("Please enter your weight (in kg):")
    await UserState.weight.set()


@dp.message_handler(state=UserState.weight)
async def send_calories(message: types.Message, state: FSMContext):
    await state.update_data(weight=message.text)
    data = await state.get_data()
    age = int(data['age'])
    height = int(data['growth'])
    weight = int(data['weight'])
    calorie_norm = 10 * weight + 6.25 * height - 5 * age + 5
    await message.answer(f"Your daily calorie intake should be: {calorie_norm:.2f} kcal.")
    await state.finish()


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
