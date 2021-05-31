from SheebaQueen.events import register
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ParseMode, Update


@register(pattern="^/game")

async def game(event): 

      await event.reply("/2048") 

__mod_name__ = " Games "

__help__ = """ COMING SOON..... """
