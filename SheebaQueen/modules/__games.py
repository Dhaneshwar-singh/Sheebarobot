from SheebaQueen.events import register
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


@register(pattern="^/game")

async def game(event): 

      await event.reply("/2048 : 2048 No. making game") 
#2048 game
f_img="https://telegra.ph/file/dbe8d49976baf292bb372.png"

@register(pattern="^/2048")

async def game(event): 

      await event.reply(f_img,
                 reply_markup=InlineKeyboardMarkup(

            [

                [

                    InlineKeyboardButton(

                        "🎶 Lightning Music Player", url="https://sheebaga.heliohost.us"

                    )

                ] ] )
         
      
      
      
                       ) 











