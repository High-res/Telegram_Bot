from src.echoBot.echoBirthday import get_birthday_name, send_birthday
from src.mainFunctions.currentDate import hour_minute_now, hours_to_minutes
from src.mainFunctions.sendMessage import send_message


birthday_send_time = '09:00'
print('Worked birday.py')
async def if_send() :
    if (hours_to_minutes(birthday_send_time)*60) == (hours_to_minutes(hour_minute_now())*60):
        with open('birthday.txt', 'w') as file:
            file.write(hour_minute_now())
        if get_birthday_name():
            await send_birthday()
        else:
            print('Сегодня нет дней рождений')

