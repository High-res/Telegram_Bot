import asyncio
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage

import config


print('Worked main file')
loop = asyncio.get_event_loop()
bot = Bot(config.MAIN_BOT_API, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot, storage=MemoryStorage())


if __name__ == "__main__":
    from src.menu.menu import dp
    from src.schedulers.botAutoSend import bot_auto_send_schedule_to_main
    from src.schedulers.birthday import birthday_schedule
    from src.schedulers.challenge import challenge_scheduler
    loop.create_task(bot_auto_send_schedule_to_main())
    loop.create_task(birthday_schedule())
    loop.create_task(challenge_scheduler())
    executor.start_polling(dp, skip_updates=True)
        