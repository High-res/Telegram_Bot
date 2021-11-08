from apscheduler.schedulers.asyncio import AsyncIOScheduler
import asyncio

from src.challengeDependency.challengeMarkup import challenge
from src.echoBot.echoChallenge import echoChallenge
from src.mainFunctions.currentDate import hour_minute_now, current_date


print(challenge())
async def botScheduler():
    print('Challenge')
    print(current_date())
    if challenge():
        if challenge()['send_time_1'] == hour_minute_now():
            await echoChallenge()
