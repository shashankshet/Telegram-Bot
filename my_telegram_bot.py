import asyncio
from telegram import Bot

bot_token = '<Bot_token>'
chat_id = '<CHAT_ID>'


bot = Bot(token=bot_token)


message = '<message>'

async def send_message():
    await bot.send_message(chat_id=chat_id, text=message)


async def run_bot():
    while True:
        await send_message()
        await asyncio.sleep(5)

loop = asyncio.get_event_loop()
loop.run_until_complete(run_bot())
