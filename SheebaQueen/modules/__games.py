from SheebaQueen.events import register
from telethon import Button

@register(pattern="^/game")

async def game(event): 

      await event.reply("/no : makin 2048 no.")
#2048 game
f_img= "http://sheebaga.heliohost.us"

@register(pattern="^/no")

async def no(event): 

      await event.reply(f_img, buttons = [[
Button.url("2048 No. Game" , url ="sheebaga.heliohost.us")

]]  )                

