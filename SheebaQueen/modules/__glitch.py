import os
from MediaInfo import MediaInfo
from SheebaQueen.events import register


@register(pattern="^/glitch$")
async def _(e):
    reply = await e.get_reply_message()
    if not (reply and reply.media):
            (e, "Reply to any media")
    wut = (reply)
    if not .startswith(("pic", "sticker")):
        return await (e, "`Unsupported Media`")
    xx = await (e, "`Gliching...`")
    ok = await bot.download_media(reply.media)
    cmd = f"glitch_me gif --line_count 200 -f 10 -d 50 '{ok}' ult.gif"
    stdout, stderr = await bash(cmd)
    await ultroid_bot.send_file(
        e.chat_id, "ult.gif", force_document=False, reply_to=reply
    )
    await xx.delete()
    os.remove(ok)
    os.remove("ult.gif")
