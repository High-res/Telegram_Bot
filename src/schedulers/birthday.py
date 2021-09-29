import asyncio
import aioschedule
from datetime import datetime, timedelta
import time

from src.echoBot.echoBirthday import get_birthday_name, send_birthday

print('Worked birday.py')
async def if_send() :
    if get_birthday_name() :
        await send_birthday()
    else :
        print('Сегодня нет дней рождений')


async def birthday_schedule():
    # aioschedule.every().day.at('10:00').do(if_send)
    while True:
        # await aioschedule.run_pending()
        hour = 10
        minute = 00
        now = datetime.now()
        future = datetime(now.year, now.month, now.day, hour, minute)
        if now.hour == hour and now.minute == minute:
            future += timedelta(days=1)
        await asyncio.sleep((future-now).seconds)
        await if_send()

