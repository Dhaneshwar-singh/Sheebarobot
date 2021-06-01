from SheebaQueen.events import register
from telegram import InlineKeyboardButton, InlineKeyboardMarkup


@register(pattern="^/game")

async def game(event): 

      await event.reply("/no : makin 2048 no.")
#2048 game
f_img="https://telegra.ph/file/dbe8d49976baf292bb372.png"

@register(pattern="^/no")

async def no(event): 

      await event.reply(f_img, [
    [
        InlineKeyboardButton(
            text="2048", url="sheebaga.heliohost.com")
    ]

])
                  

