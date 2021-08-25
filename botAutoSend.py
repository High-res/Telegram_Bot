import asyncio
import aioschedule
import time
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from datetime import datetime
from aiogram.utils import executor
import config
import actions
from main import sendToWorkers


loop = asyncio.get_event_loop()
msg_date = []
msg_date_now = []
tg_id = []

print('BotAutoSend Worked')
def currentDate() : 
    current_datetime = datetime.now().strftime('%Y-%m-%dT%H:%M')

    return current_datetime

def getText():
    get_text = actions.getText()

    return get_text



def getMsgDateNow() :
    for i in range(len(getText())) :
        msg_date_now.append(getText()[i]['msg_date'])
    
    return msg_date_now




            
async def aioScheduler():
    if currentDate() in getMsgDateNow() :
        await sendToWorkers()
        return
    else :
        print('Работает каждые 50 секунд')
    
async def botScheduler():
    aioschedule.every(50).seconds.do(aioScheduler)
    while True:
        await aioschedule.run_pending()
        time.sleep(1)

    
if __name__ == "__main__" :
    while True :
        asyncio.run(botScheduler())