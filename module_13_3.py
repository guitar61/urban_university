from aiogram import Bot, executor, Dispatcher, types


# Insert your bot's API token here
API_TOKEN = ""


bot = Bot(API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    # Send a message in the Telegram chat
    await message.answer("Hello! I'm a bot helping your health.")


# Handler for all other messages
@dp.message_handler()
async def all_messages(message: types.Message):
    # Send a message in the Telegram chat
    await message.answer("Please enter /start to begin chatting.")


# Start polling (listening for new messages)
if __name__ == '__main__':
    print("Bot is running...")
    executor.start_polling(dp, skip_updates=True)