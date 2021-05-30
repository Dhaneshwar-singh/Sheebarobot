from SheebaQueen import telethn as game
from SheebaQueen.events import register
from telethon import types, Button, events


@game.on(events.NewMessage(pattern="^/game ? (.*)"))
async def game (event):
 return await event.respond("hello, this is message")

__mode_name = " Games "
__help__ = """ 
COMING SOON..... """
