import asyncio
from pytz import utc
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from apscheduler.schedulers.asyncio import AsyncIOScheduler

import config


print('Worked main file')
loop = asyncio.get_event_loop()
bot = Bot(config.MAIN_BOT_API, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot, storage=MemoryStorage())



if __name__ == "__main__":
    from src.menu.menu import dp
    from src.schedulers.challenge import botScheduler
    from src.schedulers.botAutoSend import bot_auto_send_schedule
    from src.schedulers.birthday import if_send
    scheduler = AsyncIOScheduler()
    scheduler.add_job(botScheduler, 'interval', seconds=60)
    scheduler.add_job(bot_auto_send_schedule, 'interval', seconds=60)
    scheduler.add_job(if_send, 'interval', seconds=60)
    scheduler.start()
    executor.start_polling(dp, skip_updates=False)
        