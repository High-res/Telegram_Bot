import asyncio

from src.challengeDependency.challengeMarkup import challenge
from src.echoBot.echoChallenge import echoChallenge


async def challenge_scheduler():
    if challenge():
        # aioschedule.every().day.at(challenge()['send_time_1']).do(echoChallenge)
        while True:
            await asyncio.sleep(1)
            # await aioschedule.run_pending()
            await echoChallenge()
    else:
        # aioschedule.every(1).minutes.do(challenge_scheduler)
        while True:
            # await aioschedule.run_pending()
            await asyncio.sleep(60)
            await challenge_scheduler()
