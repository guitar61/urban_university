from aiogram import Bot, Dispatcher, executor, types
import asyncio

# Your bot token from BotFather (keep this secure and don't commit it to GitHub)
API_TOKEN = ""

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

# Define the start command handler
@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    print("Hello! I'm a bot helping your health.")
    await message.reply("Hello! I'm a bot helping your health.")

# Define a handler for all other messages
@dp.message_handler()
async def all_messages(message: types.Message):
    print("Enter /start to start a chat.")
    await message.reply("Enter /start to start a chat.")

# Main function to start the bot
if __name__ == "__main__":
    print("Bot is starting...")
    executor.start_polling(dp, skip_updates=True)