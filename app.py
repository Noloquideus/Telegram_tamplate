from aiogram import executor
from loader import bot, dp
from data import ADMIN
from handlers import setup


async def on_startup(_):
    await bot.send_message(ADMIN, "Bot is ready")
    print("Bot is working")


if __name__ == '__main__':
    setup(dp)
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
