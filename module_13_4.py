from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
import os


API_TOKEN = ""

bot = Bot(API_TOKEN)
storage = MemoryStorage()  # Store FSM states in memory
dp = Dispatcher(bot, storage=storage)


class UserState(StatesGroup):
    age = State()  # Expecting the user's age
    growth = State()  # Expecting the user's height
    weight = State()  # Expecting the user's weight



@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer("Hello I am a bot helping your health\n")


@dp.message_handler(text="Calories")
async def set_age(message: types.Message):
    await message.answer("Enter your age:")
    await UserState.age.set()  # Set the state to age, waiting for the user to input their age


@dp.message_handler(state=UserState.age)
async def set_growth(message: types.Message, state: FSMContext):
    # Store the user's age in FSM context
    await state.update_data(age=message.text)

    # Ask for the user's height
    await message.answer("Enter your height (in cm):")
    await UserState.growth.set()  # Set the state to growth (height)


@dp.message_handler(state=UserState.growth)
async def set_weight(message: types.Message, state: FSMContext):
    # Store the user's height in FSM context
    await state.update_data(growth=message.text)

    # Ask for the user's weight
    await message.answer("Enter your weight (in kg):")
    await UserState.weight.set()  # Set the state to weight


@dp.message_handler(state=UserState.weight)
async def send_calories(message: types.Message, state: FSMContext):
    # Store the user's weight in FSM context
    await state.update_data(weight=message.text)

    # Retrieve all data (age, height, weight)
    data = await state.get_data()
    age = int(data['age'])
    height = int(data['growth'])
    weight = int(data['weight'])

    # Calculate calorie intake using the Mifflin-St Jeor formula
    # For simplicity, let's assume this is for men (change if needed)
    calorie_norm = 10 * weight + 6.25 * height - 5 * age + 5

    # Send the calculated calorie intake to the user
    await message.answer(f"Your daily calorie intake should be: {calorie_norm} kcal.")

    # Finish the state machine
    await state.finish()


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

