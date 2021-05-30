from SheebaQueen.events import register
@register(pattern="^/game ? (.*)")
async def game (event): 
    await event.reply("hello, this is message") 
__mod_name__ = " Games "
__help__ = """ COMING SOON..... """
