from src.echoBot.echoMessage import sendToWorkers
from src.db_connect.getText import get_text
from src.mainFunctions.currentDate import current_date


msg_date = []
msg_date_now = []
tg_id = []

print('BotAutoSend Worked')
def get_text_msg():
    get_textes = get_text()

    return get_textes

def get_msg_date_now() :
    for i in range(len(get_text_msg())) :
        msg_date_now.append(get_text_msg()[i]['msg_date'])
    
    return msg_date_now
         
async def bot_auto_send_schedule():
    print('BotAutoSend')
    if current_date() in get_msg_date_now() :
        await sendToWorkers()
        # return


