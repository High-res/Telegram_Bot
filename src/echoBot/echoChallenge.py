from src.challengeDependency.challengeMarkup import challenge, challenge_workers
from src.mainFunctions.AllWorkersTgID import all_workers_tg_id
from src.markups.markups import button_challenge


# print(challenge_workers())
async def echoChallenge() :
    from main import bot
    if challenge():
        for i in all_workers_tg_id():
            try:
                await bot.send_message(i, challenge()['challenge'], reply_markup=button_challenge())
                print(i)
            except Exception as ex:
                print(ex)
    all_workers_tg_id().clear()