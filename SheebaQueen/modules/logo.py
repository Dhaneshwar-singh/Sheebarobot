
import os
import random

import requests
from bs4 import *
from pyrogram import filters

from SheebaQueen.pyrogramee.pluginshelper import admins_only, get_text
from SheebaQueen.resources.pyrogram import pbot


def download_images(images):
    count = 0
    print(f"Total {len(images)} Image Found!")
    if len(images) != 0:
        for i, image in enumerate(images):
            try:
                image_link = image["data-srcset"]
            except:
                try:
                    image_link = image["data-src"]
                except:
                    try:
                        image_link = image["data-fallback-src"]
                    except:
                        try:
                            image_link = image["src"]
                        except:

                            pass
            try:
                r = requests.get(image_link).content
                try:

                    r = str(r, "utf-8")
                except UnicodeDecodeError:
                    with open("logo@AsunaBOT.jpg", "wb+") as f:
                        f.write(r)
                    count += 1
            except:
                pass


def mainne(name, typeo):
    url = f"https://source.unsplash.com/random={name}&searchtext={typeo}&searchService="
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")
    images = soup.findAll("img")
    random.shuffle(images)
    if images is not None:
        print("level 1 pass")
    download_images(images)


@pbot.on_message(filters.command("logo") & ~filters.edited & ~filters.bot)
@admins_only
async def logogen(client, message):
    pablo = await client.send_message(message.chat.id, "`Creating The Logo.....`")
    Godzilla = get_text(message)
    if not Godzilla:
        await pablo.edit("Invalid Command Syntax, Please Check Help Menu To Know More!")
        return
    lmao = Godzilla.split(":", 1)
    try:
        typeo = lmao[1]
    except BaseException:
        typeo = "name"
        await pablo.edit(
            "Give name and type for logo Idiot. like `/logogen Made By Asuna_Robot`"
        )
    name = lmao[0]
    mainne(name, typeo)
    pate = "logo@AsunaBOT.jpg"
    await client.send_photo(message.chat.id, pate)
    try:
        os.remove(pate)
    except:
        pass
    await pablo.delete()
