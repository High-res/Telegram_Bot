import asyncio
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import config


print('Worked main file')
loop = asyncio.get_event_loop()
bot = Bot(config.MAIN_BOT_API, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot, loop=loop, storage=MemoryStorage())


if __name__ == "__main__" :
    from src.menu.menu import dp
    executor.start_polling(dp, loop=loop)
        