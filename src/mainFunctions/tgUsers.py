from src.actions.getUser import getUser


tg_id = []
def tgUsers() :
    tgUsers = getUser()
    for i in range(len(tgUsers)) :
        tg_id.append(tgUsers[i]['tg_id'])
    return tg_id