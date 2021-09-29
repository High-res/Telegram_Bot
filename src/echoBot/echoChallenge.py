import asyncio

from main import bot
from src.challengeDependency.challengeMarkup import challenge, challenge_workers
from src.mainFunctions.AllWorkersTgID import all_workers_tg_id
from src.markups.markups import button_challenge


async def echoChallenge() :
    for i in all_workers_tg_id() :
        await bot.send_message(i, challenge()['challenge'], reply_markup=button_challenge())
    challenge_workers().clear()
    await asyncio.sleep(60)