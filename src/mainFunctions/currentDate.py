from datetime import datetime, date, time
import time


def current_date() : 
    current_datetime = datetime.now().strftime('%Y-%m-%dT%H:%M')

    return current_datetime

def hour_minute_now():
    current_datetime = datetime.now().strftime('%H:%M')
    return current_datetime
    
def reg_date() :
    register_date = datetime.now().strftime('%Y-%m-%d')
    return register_date

def cloack_date() :
    cloak_date = datetime.strptime(time.ctime(), "%a %b %d %H:%M:%S %Y")
    return cloak_date

def get_date() :
    today = date.today()
    year = today.strftime('%Y-%m-%d')
    day = today.strftime('%Y-%m')
    return year, day

def hours_to_minutes(e) :
    if e :
        hours, minutes = e.split(':')
        multiply = int(hours) * 60
        return multiply
    else :
        print('Принял пустое значение')

def hour_minute() :
    hour = datetime.now().strftime("%m-%d")
    return hour
