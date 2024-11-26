from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from crud_functions import initiate_db, add_user, is_included

API_TOKEN = '7705129595:AAGiyBXkqlOJPML6hr5THaPlWDTEPDFeZ-U'  # Add your bot's API token

bot = Bot(token=API_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

# Initialize the database
initiate_db()

# Main menu reply keyboard with added "Registration" button
main_menu_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
button_calculate = KeyboardButton("Calculate")
button_info = KeyboardButton("Information")
button_buy = KeyboardButton("Buy")
button_register = KeyboardButton("Registration")  # New "Registration" button
main_menu_keyboard.add(button_calculate, button_info, button_buy, button_register)

# Define the state machine for user registration
class RegistrationState(StatesGroup):
    username = State()
    email = State()
    age = State()

# /start command handler to display the main menu
@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer(
        "Welcome! Choose an option from the menu.",
        reply_markup=main_menu_keyboard
    )

# Registration start handler
@dp.message_handler(text="Registration")
async def sing_up(message: types.Message):
    await message.answer("Please enter your username (use only Latin alphabet):")
    await RegistrationState.username.set()

# Username handler
@dp.message_handler(state=RegistrationState.username)
async def set_username(message: types.Message, state: FSMContext):
    username = message.text
    if is_included(username):
        await message.answer("The username already exists, please choose a different one.")
        return
    await state.update_data(username=username)
    await message.answer("Please enter your email:")
    await RegistrationState.email.set()

# Email handler
@dp.message_handler(state=RegistrationState.email)
async def set_email(message: types.Message, state: FSMContext):
    email = message.text
    await state.update_data(email=email)
    await message.answer("Please enter your age:")
    await RegistrationState.age.set()

# Age handler
@dp.message_handler(state=RegistrationState.age)
async def set_age(message: types.Message, state: FSMContext):
    age = int(message.text)
    data = await state.get_data()
    username = data['username']
    email = data['email']
    add_user(username, email, age)
    await message.answer("Registration successful!")
    await state.finish()

# Other existing handlers...

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
