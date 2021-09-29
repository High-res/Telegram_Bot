import aioschedule
import asyncio
from datetime import datetime
import time

from src.echoBot.echoMessage import sendToWorkers
from src.db_connect.getText import get_text
from src.mainFunctions.currentDate import current_date


msg_date = []
msg_date_now = []
tg_id = []

print('BotAutoSend Worked')
print(current_date())
DELAY = 60
def get_text_msg():
    get_textes = get_text()

    return get_textes

def get_msg_date_now() :
    for i in range(len(get_text_msg())) :
        msg_date_now.append(get_text_msg()[i]['msg_date'])
    
    return msg_date_now
         
async def bot_auto_send_schedule():
    if current_date() in get_msg_date_now() :
        await sendToWorkers()
        # return
    else :
        print('Работает каждую 1 минуту')
        print(current_date())
        print(DELAY)

async def bot_auto_send_schedule_to_main():
    # aioschedule.every(1).minutes.do(bot_auto_send_schedule)
    while True:
        # await asyncio.sleep(60)
        # await aioschedule.run_pending()
        await asyncio.sleep(DELAY)
        await bot_auto_send_schedule()


