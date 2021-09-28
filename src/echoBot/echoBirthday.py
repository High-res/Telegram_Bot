from datetime import date
from src.actions.getWorker import getWorkerss
from src.mainFunctions.sendMessage import send_message


# Birthday send message
user = []
bday_user = []
all_tg_id = []

def bDay() :
    today = date.today()
    bday = today.strftime('%m-%d')
    return bday


def takeWorkers() :
    workers = getWorkerss()
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