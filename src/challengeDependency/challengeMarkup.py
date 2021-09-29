from src.db_connect.getChallenge import get_challenge, get_challenge_action


def challenge() :
    if get_challenge() :
        challenge = get_challenge()
        if challenge :
            return challenge[-1]

challengeTgId = []
    
def challenge_workers() :
    challengeWork = get_challenge_action()
    for i in challengeWork :
        challengeTgId.append(i['tg_id'])

    return challengeTgId

