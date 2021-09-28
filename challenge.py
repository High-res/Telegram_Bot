import aioschedule
import time
import asyncio
from src.challengeDependency.challengeMarkup import challenge
from src.echoBot.echoChallenge import echoChallenge

print(challenge())

async def botScheduler():
    if challenge()['send_time_1'] :
        aioschedule.every().day.at(challenge()['send_time_1']).do(echoChallenge)
    while True:
        await aioschedule.run_pending()
        time.sleep(1)

if __name__ == "__main__" :
    while True :
        asyncio.run(botScheduler())