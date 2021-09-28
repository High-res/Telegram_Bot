from src.actions.getText import getText


msg_date = []
msg_date_now = []
def getText():
    get_text = getText()

    return get_text

def getMsgDate() :
    for i in range(len(getText())) :
        msg_date.append(getText()[i])
    
    return msg_date



def getMsgDateNow() :
    for i in range(len(getText())) :
        msg_date_now.append(getText()[i]['msg_date'])
    
    return msg_date_now