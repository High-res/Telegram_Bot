from src.db_connect.getText import get_text


msg_date = []
msg_date_now = []
def get_text_message():
    get_text_msg = get_text()

    return get_text_msg

def getMsgDate() :
    for i in range(len(get_text_message())) :
        msg_date.append(get_text_message()[i])
    
    return msg_date



def getMsgDateNow() :
    for i in range(len(get_text_message())) :
        msg_date_now.append(get_text_message()[i]['msg_date'])
    
    return msg_date_now