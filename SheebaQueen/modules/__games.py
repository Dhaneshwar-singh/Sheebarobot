from SheebaQueen import pbot
@pbot.on_message(filters.command("game") & ~filters.edited & ~filters.bot)

async def game(client, message):

    await message.reply("`Processing.....`")
#a@register(pattern="^/game ? (.*)")
#async def game (event): 
   # await event.reply("hello, this is message")# 
__mod_name__ = " Games "
__help__ = """ COMING SOON..... """
