from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import asyncio

import config


loop = asyncio.get_event_loop()
bot = Bot(config.MAIN_BOT_API, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot, loop=loop, storage=MemoryStorage())


@dp.message_handler()
async def send_docx_to_root(e) :
    py_docx_file = open(e, 'rb')
    await bot.send_document(958557779, py_docx_file)