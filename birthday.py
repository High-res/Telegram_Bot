import asyncio
import aioschedule
import time
from main import send_birthday, get_birthday_name

print('Worked birday.py')
async def ifSend() :
    if get_birthday_name() :
        await send_birthday()
    else :
        print('Сегодня нет дней рождений')


async def birthdaySchedule():
    aioschedule.every().day.at('09:00').do(ifSend)
    while True:
        await aioschedule.run_pending()
        time.sleep(1)


if __name__ == "__main__" :
    while True :
        asyncio.run(birthdaySchedule())