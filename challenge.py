import aioschedule
import time
import asyncio
import markup
from main import echoChallenge

print(markup.challenge())

async def botScheduler():
    aioschedule.every().day.at('17:00').do(echoChallenge)
    while True:
        await aioschedule.run_pending()
        time.sleep(1)

if __name__ == "__main__" :
    while True :
        asyncio.run(botScheduler())