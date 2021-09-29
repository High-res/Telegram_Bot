from src.db_connect.getWorker import get_workerss
from src.db_connect.getChallenge import get_challenge_action
from src.challengeDependency.challengeMarkup import challenge
from src.db_connect.getUser import get_user
from src.mainFunctions.currentDate import hours_to_minutes, hour_minute


allWorkersID = []
def all_workers_tg_id() :
    getAllWorkers = get_workerss()
    for j in range(len(getAllWorkers)) :
        if getAllWorkers[j]['tg_id'] != 0 :
            allWorkersID.append(getAllWorkers[j]['tg_id'])
    
    return allWorkersID


challengeTgID = []
def get_challenge_action_tg_id() :
    TgID = get_challenge_action()
    for i in TgID :
        if challenge()['send_time_1'] :
            if hours_to_minutes(hour_minute()) > hours_to_minutes(challenge()['send_time_1']) :
                challengeTgID.append(i['tg_id'])
    return challengeTgID

tg_id = []
def tg_users() :
    tgUsers = get_user()
    for i in range(len(tgUsers)) :
        tg_id.append(tgUsers[i]['tg_id'])
    return tg_id


user = []
def take_workers() :
    workers = get_workerss()
    for i in workers :
        user.append(i)
    return user
