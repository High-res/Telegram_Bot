import asyncio
import json
from aiogram.dispatcher.filters.builtin import Command
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from datetime import datetime
from datetime import date
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from markups import getDataMark
import markup
import markups as nav
import config
import actions


print('Worked main file')
loop = asyncio.get_event_loop()
bot = Bot(config.MAIN_BOT_API, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot, loop=loop, storage=MemoryStorage())
message = types.Message
tg_id = []
msg_date = []
msg_date_now = []


def getWorkerTgID() :
    allWorkers = actions.getWorkerss()
    for w in range(0, len(allWorkers)) :
        if allWorkers[w]['tg_id'] != 0 :
            tg_id.append(allWorkers[w]['tg_id'])
    return tg_id

def currentDate() : 
    current_datetime = datetime.now().strftime('%Y-%m-%dT%H:%M')

    return current_datetime

def getText():
    get_text = actions.getText()

    return get_text

def getMsgDate() :
    for i in range(len(getText())) :
        msg_date.append(getText()[i])
    
    return msg_date



def getMsgDateNow() :
    for i in range(len(getText())) :
        msg_date_now.append(getText()[i]['msg_date'])
    
    return msg_date_now


def RegDate() :
    register_date = datetime.now().strftime('%Y-%m-%d')
    return register_date
# Дата регистрации пользователя register_date
# print(cloak_date)
tg_id = []
def tgUsers() :
    tgUsers = actions.getUser()
    for i in range(len(tgUsers)) :
        tg_id.append(tgUsers[i]['tg_id'])
    return tg_id
    

@dp.message_handler(Command("start"))
async def start_command(message: types.Message): 
    userName = message.from_user.first_name
    userID = message.from_user.id
    if userID in tgUsers() :
        print('Такой пользователь существует')
    else :
        actions.addUser(userName, userID, RegDate())
    tgUsers().clear()
    await bot.send_message(message.from_user.id, getDataMark()['glavnaya']['main_text'], reply_markup=nav.mainMenu)
    


# Auto send message
async def send_message(channel_id: int, text: str):
    await bot.send_message(channel_id, text)

def sendText() :
    for x in getMsgDate() :
        if currentDate() in x['msg_date'] :
            messageTextSend = x['msg_text']
            print('Здесь сработало!')
    return messageTextSend


async def sendToWorkers() :
    if sendText() :
        for i in getWorkerTgID() :
            print(i)
            await send_message(channel_id=i, text = sendText())
    getWorkerTgID().clear()
    # else :
    #     print('Не сработало')
        
# Birthday send message
user = []
bday_user = []
all_tg_id = []

def bDay() :
    today = date.today()
    bday = today.strftime('%m-%d')
    return bday

def takeWorkers() :
    workers = actions.getWorkerss()
    for i in workers :
        user.append(i)
    return user
    

def get_birthday_name() :
    for row in takeWorkers() :
        # print(row)
        if bDay() == row['b_day'] :
            # print(row)
            bday_user = row
            bday_user_name = bday_user['name']
            bday_user_tg_id = bday_user['tg_id']
    takeWorkers().clear()
    if bday_user_name :
        return bday_user_name, bday_user_tg_id, bday_user
    else :
        print('Надо смотреть как работает')


def get_workers_id() :
        # print(takeWorkers())
    if get_birthday_name()[2] :
        name = get_birthday_name()[2]
        for ro in takeWorkers() :
            if name != ro:
                print(ro)
                if ro['tg_id'] != 0 :
                    all_tg_id.append(ro['tg_id'])
        takeWorkers().clear()
        return all_tg_id
    else :
        print('Здесь остановим функцию')
    

async def send_birthday() :
    if get_birthday_name()[0] :
        for i in get_workers_id() :
            await send_message(channel_id = i, text = f'Сегодня день рождение у {get_birthday_name()[0]}')
    else :
        print('Not today!')

async def echoChallenge() :
    # await bot.send_message(config.ADMIN_ID, markup.challenge()['challenge'], reply_markup=nav.buttonChallenge())
    for i in getWorkerTgID() :
        await bot.send_message(i, markup.challenge()['challenge'], reply_markup=nav.buttonChallenge())
    markup.challengeWorkers().clear()


if __name__ == "__main__" :
    from menu import dp
    # executor.start_polling(dp, loop=loop, on_startup = onStartup)
    executor.start_polling(dp, loop=loop)
        