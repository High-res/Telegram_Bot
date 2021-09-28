from datetime import datetime


def currentDate() : 
    current_datetime = datetime.now().strftime('%Y-%m-%dT%H:%M')

    return current_datetime

    

def RegDate() :
    register_date = datetime.now().strftime('%Y-%m-%d')
    return register_date