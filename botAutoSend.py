import asyncio
import aioschedule
import time
from datetime import datetime
import actions
from main import sendToWorkers


msg_date = []
msg_date_now = []
tg_id = []

print('BotAutoSend Worked')
def currentDate() : 
    current_datetime = datetime.now().strftime('%Y-%m-%dT%H:%M')

    return current_datetime

print(currentDate())
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
        # return
    else :
        print('Работает каждую 1 минуту')
        print(currentDate())
    
async def botScheduler():
    aioschedule.every(1).minutes.do(aioScheduler)
    while True:
        await aioschedule.run_pending()
        time.sleep(1)

    
if __name__ == "__main__" :
    while True :
        asyncio.run(botScheduler())