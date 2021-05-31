from SheebaQueen.events import register
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


@register(pattern="^/game")

async def game(event): 

      await event.reply("/2048 : 2048 No. making game") 

__mod_name__ = " Games "

__help__ = """ COMING SOON..... """
