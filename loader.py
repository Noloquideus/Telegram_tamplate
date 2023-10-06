from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from data import TOKEN

# Create a bot instance
bot = Bot(token=TOKEN)
# Create a dispatcher instance
dp = Dispatcher(bot, storage=MemoryStorage())