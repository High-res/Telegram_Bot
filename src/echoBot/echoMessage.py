from src.mainFunctions.currentDate import current_date
from src.mainFunctions.getMsgDate import getMsgDate
from src.mainFunctions.AllWorkersTgID import all_workers_tg_id
from src.mainFunctions.sendMessage import send_message


# Отложенные сообщения
def sendText() :
    for x in getMsgDate() :
        if current_date() in x['msg_date'] :
            messageTextSend = x['msg_text']
            print('Здесь сработало!')
    return messageTextSend


async def sendToWorkers() :
    if sendText() :
        for i in all_workers_tg_id() :
            try:
                await send_message(channel_id=i, text = sendText())
                print(i)
            except Exception as ex:
                print(ex)
    all_workers_tg_id().clear()
    # else :
    #     print('Не сработало')
        