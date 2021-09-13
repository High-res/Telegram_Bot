import aioschedule
import time
import asyncio
import markup
from main import echoChallenge

print(markup.challenge())

async def botScheduler():
    if markup.challenge()['send_time_1'] :
        aioschedule.every().day.at(markup.challenge()['send_time_1']).do(echoChallenge)
    while True:
        await aioschedule.run_pending()
        time.sleep(1)

if __name__ == "__main__" :
    while True :
        asyncio.run(botScheduler())