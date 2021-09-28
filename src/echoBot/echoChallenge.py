from src.challengeDependency.challengeMarkup import challenge, challengeWorkers
from src.mainFunctions.AllWorkersTgID import AllWorkersTgID
from src.markups.markups import buttonChallenge
from main import bot


async def echoChallenge() :
    # await bot.send_message(config.ADMIN_ID, markup.challenge()['challenge'], reply_markup=markups.buttonChallenge())
    for i in AllWorkersTgID() :
        await bot.send_message(i, challenge()['challenge'], reply_markup=buttonChallenge())
    challengeWorkers().clear()