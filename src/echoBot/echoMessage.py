from src.mainFunctions.currentDate import currentDate
from src.mainFunctions.getMsgDate import getMsgDate
from src.mainFunctions.AllWorkersTgID import AllWorkersTgID
from src.mainFunctions.sendMessage import send_message


# Отложенные сообщения
def sendText() :
    for x in getMsgDate() :
        if currentDate() in x['msg_date'] :
            messageTextSend = x['msg_text']
            print('Здесь сработало!')
    return messageTextSend


async def sendToWorkers() :
    if sendText() :
        for i in AllWorkersTgID() :
            print(i)
            await send_message(channel_id=i, text = sendText())
    AllWorkersTgID().clear()
    # else :
    #     print('Не сработало')
        