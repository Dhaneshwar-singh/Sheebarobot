from SheebaQueen.events import register
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


@register(pattern="^/game")

async def game(event): 

      await event.reply("/2048 : 2048 No. making game") 
#2048 game
@register(pattern="^/2048")

async def game(event): 

      await event.reply(
         reply_markup = InlineKeyboardMarkup(
         
         [InlineKeyboardButton(

                        "", url="t.me/vcmusicplayerlightning"

                    )

                ],
         
         
      
      
      
      ) 








__mod_name__ = " Games "

__help__ = """ COMING SOON..... """
