from SheebaQueen.events import register
from telethon import Button


@register(pattern="^/game")

async def game(event): 

      await event.reply("/no : makin 2048 no. /run : run game /slice : Pokeball slice game")
#2048 game

@register(pattern="^/no")

async def no(event): 

      await event.reply("Some Games By Me"
,buttons=[[Button.url("2048 game ",url="sheebaga.heliohost.us")]])
#pokemon sluce

@register(pattern="^/slice")

async def slice(event): 

      await event.reply("Some Games By Me"
,button=[[Button.url("2048 game ",url="sheebaga.heliohost.us/pokemonslice.html")]])

#Rom run

@register(pattern="^/run")

async def run(event): 

      await event.reply("Some Games By Me"
,button=[[Button.url("2048 game ",url="https://games.cdn.famobi.com/html5games/o/om-nom-run/v1140/?fg_domain=play.famobi.com&fg_aid=A1000-1&fg_uid=abe80572-560a-444d-baf7-2fa4a7b2c02f&fg_pid=4638e320-4444-4514-81c4-d80a8c662371&fg_beat=177&original_ref=android-app%3A%2F%2Forg.telegram.messenger%2F")]])



__mod_name__ = "Game"
__help__ ="""
 /game ==>> get button for all available games
"""




