
import asyncio
import os
import requests
import time
from PIL import Image
from io import BytesIO
from datetime import datetime
import random
from telethon import events
from userbot.utils import admin_cmd, sudo_cmd
from userbot import ALIVE_NAME
from telethon.tl.types import ChannelParticipantsAdmins
# ð¤ð¤ð¤ð¤ð¤ð¤ð¤ð¤ð¤ð¤ð¤ð¤ð¤ð¤ð¤ð¤ð¤ð¤ð¤ð¤ð¤ð¤ð¤ð¤ð¤ð¤ð¤ð¤ð¤
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "LEGEND SAR"
ALIVE_PHOTTO = os.environ.get("ALIVE_PHOTTO" , None)

# Thanks to Sipak bro and Raganork.. 
# animation Idea by @NOOB_GUY_OP (Sipakisking)
# Made by @hellboi_atul ....and thanks to @Crackexy for the logos...
# Kang with credits else gay...
# alive.py for DC(DARK COBRA)
global ghanti
ghanti = borg.uid
edit_time = 5
""" =======================CONSTANTS====================== """
file1 = "https://telegra.ph/file/fc22c880e9b4c74b9f33f.jpg"
file2 = "https://telegra.ph/file/fc22c880e9b4c74b9f33f.jpg"
file3 = "https://telegra.ph/file/fc22c880e9b4c74b9f33f.jpg"
file4 = "https://telegra.ph/file/fc22c880e9b4c74b9f33f.jpg"
""" =======================CONSTANTS====================== """
pm_caption = " TSF BOT IS ONLINE\n\n"
pm_caption += "Yes Master, Am Alive And Systems Are Working Perfectly As It Should Be...\n\n"
pm_caption += "â About My System â\n\n"
pm_caption += "â¾ á´á´Êá´á´Êá´É´ á´ á´Êê±Éªá´É´ â 1.18.2\n"
pm_caption += "â¾ ê±á´á´á´á´Êá´ á´Êá´É´É´á´Ê â [á´á´ÉªÉ´](https://t.me/THE_TSF_USERBOT)\n"
pm_caption += "â¾ ÊÉªá´á´É´ê±á´  â [TEAM TSF](https://t.me/tsf_gang)\n"
pm_caption += "â¾ support group â [JOIN](https://t.me/tsf_support)\n\n"
pm_caption += f"â¾ á´Ê á´á´sá´á´Ê â [{DEFAULTUSER}](tg://user?id={ghanti})\n"

@borg.on(admin_cmd(pattern=r"alive"))
@borg.on(sudo_cmd(pattern=r"alive", allow_sudo=True))

async def amireallyalive(yes):
    chat = await yes.get_chat()
    global ghanti
    ghanti = borg.uid
##
    on = await borg.send_file(yes.chat_id, file=file1,caption=pm_caption)

    await asyncio.sleep(edit_time)
    ok = await borg.edit_message(yes.chat_id, on, file=file2) 

    await asyncio.sleep(edit_time)
    ok2 = await borg.edit_message(yes.chat_id, ok, file=file3)

    await asyncio.sleep(edit_time)
    ok3 = await borg.edit_message(yes.chat_id, ok2, file=file1)
    
    await asyncio.sleep(edit_time)
    ok4 = await borg.edit_message(yes.chat_id, ok3, file=file3)
    
    await asyncio.sleep(edit_time)
    ok5 = await borg.edit_message(yes.chat_id, ok4, file=file2)
    
    await asyncio.sleep(edit_time)
    ok6 = await borg.edit_message(yes.chat_id, ok5, file=file1)
    
    await asyncio.sleep(edit_time)
    ok7 = await borg.edit_message(yes.chat_id, ok6, file=file4)

    await yes.delete()

""" For .alive command, check if the bot is running.  """
    
    

def get_readable_time(seconds: int) -> str:
    count = 0
    ping_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]

    while count < 4:
        count += 1
        if count < 3:
            remainder, result = divmod(seconds, 60)
        else:
            remainder, result = divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        ping_time += time_list.pop() + ", "

    time_list.reverse()
    ping_time += ":".join(time_list)

    return ping_time


@borg.on(admin_cmd(outgoing=True, pattern="salive"))
@borg.on(sudo_cmd(pattern=r"salive", allow_sudo=True))
async def amireallyalive(alive):
    """ For .alive command, check if the bot is running.  """
    if ALIVE_PHOTTO:
        pm_caption = "TSF Bot ð¸ð ð¾ï¸ð½ð»ð¸ð½ð´\n"
        pm_caption += f"ððª ð¹ð ð¤ð¤            : {DEFAULTUSER}\n"
        pm_caption += "ðð´ð»ð´ðð·ð¾ð½ ðð´ððð¸ð¾ð½        : 1.18.2\n"
        pm_caption += "ð¿ððð·ð¾ð½ ðð´ððð¸ð¾ð½          : 3.9.3\n"
        pm_caption += "ððð¿ð¿ð¾ðð ð²ð·ð°ð½ð½ð´ð»         : [á´á´ÉªÉ´](https://t.me/TSF_SUPPORT)\n"
        pm_caption += "ððð¿ð¿ð¾ðð ð¶ðð¾ðð¿           : [á´á´ÉªÉ´](https://t.me/THE_TSF_USERBOT)\n"
        pm_caption += "ð¾ðððððððð ð½ð            : [ TSF](https://t.me/TSF_GANG)\n"
        pm_caption += "[âââââââââââââââââââ\n âââââââââââââââââââ\n âââââââââââââââââââ\n âââââââââââââââââââ \n âââââââââ«ââââââââââ \n âââââââââââââââââââ](https://t.me/TSF_SUPPORT)"
        chat = await alive.get_chat()
        await alive.delete()
        """ For .allive command, check if the bot is running.  """
        await borg.send_file(alive.chat_id, ALIVE_PHOTTO,caption=pm_caption, link_preview = False)
        await allive.delete()
        return
    req = requests.get("(https://telegra.ph/file/fc22c880e9b4c74b9f33f.jpg")
    req.raise_for_status()
    file = BytesIO(req.content)
    file.seek(0)
    img = Image.open(file)
    with BytesIO() as sticker:
        img.save(sticker, "webp")
        sticker.name = "sticker.webp"
        sticker.seek(0)
        await borg.send_file(alive.chat_id, file=sticker)
        await borg.send_message(alive.chat_id,"TSF Bot ð¸ð ð¾ï¸ð½ð»ð¸ð½ð´\n"
                      f"ððª ð¹ð ð¤ð¤            : {DEFAULTUSER}\n"
        pm_caption += "ðð´ð»ð´ðð·ð¾ð½ ðð´ððð¸ð¾ð½        : 1.18.2\n"
        pm_caption += "ð¿ððð·ð¾ð½ ðð´ððð¸ð¾ð½          : 3.9.3\n"
        pm_caption += "ððð¿ð¿ð¾ðð ð²ð·ð°ð½ð½ð´ð»         : [á´á´ÉªÉ´](https://t.me/TSF_SUPPORT)\n"
        pm_caption += "ððð¿ð¿ð¾ðð ð¶ðð¾ðð¿           : [á´á´ÉªÉ´](https://t.me/THE_TSF_USERBOT)\n"
        pm_caption += "ð¾ðððððððð ð½ð            : [ TSF](https://t.me/TSF_GANG)\n"
        pm_caption += "[âââââââââââââââââââ\n âââââââââââââââââââ\n âââââââââââââââââââ\n âââââââââââââââââââ \n âââââââââ«ââââââââââ \n âââââââââââââââââââ](https://t.me/TSF_SUPPORT)"" , link_preview = False) 
        await alive.delete()
