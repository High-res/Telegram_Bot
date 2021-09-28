from main import bot


# Auto send message
async def send_message(channel_id: int, text: str):
    await bot.send_message(channel_id, text)