from datetime import date

from src.mainFunctions.sendMessage import send_message
from src.mainFunctions.AllWorkersTgID import take_workers


# Birthday send message
bday_user = []
all_tg_id = []

def birthday() :
    today = date.today()
    bday = today.strftime('%d-%m')
    return bday

print(f'Дата дня рождения '+birthday())
    

def get_birthday_name() :
    for row in take_workers() :
        # print(row)
        if birthday() == row['b_day'] :
            # print(row)
            bday_user = row
            bday_user_name = bday_user['name']
            bday_user_tg_id = bday_user['tg_id']
            return bday_user_name, bday_user_tg_id, bday_user
    take_workers().clear()


def get_workers_id() :
        # print(takeWorkers())
    if get_birthday_name() :
        name = get_birthday_name()[2]
        for ro in take_workers() :
            if name != ro:
                if ro['tg_id'] != 0 :
                    all_tg_id.append(ro['tg_id'])
        take_workers().clear()
        return all_tg_id
    else :
        print('Здесь остановим функцию')
    

async def send_birthday() :
    if get_birthday_name()[0] :
        for i in get_workers_id() :
            try:
                print(i)
                await send_message(channel_id = i, text = f'Сегодня день рождение у {get_birthday_name()[0]}')
            except Exception as ex:
                print(ex)
        get_workers_id().clear()
    else :
        print('Not today!')