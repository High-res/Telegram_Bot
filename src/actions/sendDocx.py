import asyncio
from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import config


loop = asyncio.get_event_loop()
bot = Bot(config.MAIN_BOT_API, parse_mode='HTML')
dp = Dispatcher(bot, loop=loop, storage=MemoryStorage())
@dp.message_handler()
async def send_docx(doc_name) :
    doc = open(doc_name, 'rb')
    await bot.send_document(958557779, doc)

