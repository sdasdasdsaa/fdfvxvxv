import json
from pyrogram import Client, idle
from pyromod import listen
from pyrogram.types import ChatPrivileges, ChatPermissions

#
#==================================================
#
#███████╗███████╗██████╗  ██████╗ 
#╚══███╔╝██╔════╝██╔══██╗██╔═══██╗
#  ███╔╝ █████╗  ██████╔╝██║   ██║
# ███╔╝  ██╔══╝  ██╔══██╗██║   ██║
#███████╗███████╗██║  ██║╚██████╔╝
#╚══════╝╚══════╝╚═╝  ╚═╝ ╚═════╝ 
#
#==================================================

bot = Client(
    "m4o",
    api_id=31681257,
    api_hash="ac78c30e1f8498af7fc782630348dcaa",
    bot_token="8845386071:AAH8-_XjezIDvzj4U2foWIhdzGqy6qMd3mE",
    plugins=dict(root="MZombie")
    )


with open('/root/baron/config.json', 'r', encoding='utf-8') as file:
    config = json.load(file)


sourse_dev = config['sourse_dev']


DEVS = []
DEVS.append(7807482327)
owner_id = sourse_dev
bot_id = bot.bot_token.split(":")[0]


async def start_zombiebot():
    await bot.start()
    for hh in DEVS:
        try:
            await bot.send_message(hh, f"**◍ تم تشغيل الصانع بنجاح 🚦\n√**")
        except:
            pass
    await idle()

#
#==================================================
#
#███████╗███████╗██████╗  ██████╗ 
#╚══███╔╝██╔════╝██╔══██╗██╔═══██╗
#  ███╔╝ █████╗  ██████╔╝██║   ██║
# ███╔╝  ██╔══╝  ██╔══██╗██║   ██║
#███████╗███████╗██║  ██║╚██████╔╝
#╚══════╝╚══════╝╚═╝  ╚═╝ ╚═════╝ 
#
#==================================================