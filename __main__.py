import asyncio
loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)

from pyrogram import idle
from .config import Config
from . import bot, ass
bot.start()
if Config.PYRO_SESSION:
   ass.start()
idle()
bot.stop()
