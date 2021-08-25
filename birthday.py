import asyncio
import aioschedule
import time
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from datetime import date
import config
import actions
from main import send_birthday

print('Worked birday.py')

async def birthdaySchedule():
    aioschedule.every().day.at('10:00').do(send_birthday)
    while True:
        await aioschedule.run_pending()
        time.sleep(1)


if __name__ == "__main__" :
    while True :
        asyncio.run(birthdaySchedule())