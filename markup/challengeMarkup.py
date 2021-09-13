import actions
from datetime import datetime

def challenge() :
    challenge = actions.getChallenge()
    if challenge :
        return challenge[-1]

challengeTgId = []
    
def challengeWorkers() :
    challengeWork = actions.getChallengeAction()
    for i in challengeWork :
        challengeTgId.append(i['tg_id'])

    return challengeTgId

def hoursToMinutes(e) :
    if e :
        hours, minutes = e.split(':')
        multiply = int(hours) * 60
        return multiply
    else :
        print('Принял пустое значение')

def HourMinute() :
    hour = datetime.now().strftime("%m-%d")
    return hour

print(HourMinute())