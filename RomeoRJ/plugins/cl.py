import os
import re
import asyncio
import time
from pyrogram import *
from pyrogram.types import *
from RomeoRJ import robot as app
from RomeoRJ.config import API_ID, API_HASH 

#cloner
@app.on_message(filters.private & filters.command("cl", ["/", ".", "!"]))
async def cl(app, message):
    k = await message.reply_text("Usage:\n\n`/cl` pyro-session")
    STRING_SESSION = message.command[1]
    try:
        await k.edit("Booting Your Client")
        r = Client(STRING_SESSION, API_ID, API_HASH, plugins=dict(root="RomeoRJ.plugins"))
        await r.start()
        user = await r.get_me()
        await k.edit(f"""
 𝐘𝐨𝐮𝐫 𝐂𝐥𝐢𝐞𝐧𝐭 𝐇𝐚𝐬 𝐁𝐞𝐞𝐧 𝐒𝐮𝐜𝐜𝐞𝐬𝐟𝐮𝐥𝐥𝐲 𝐒𝐭𝐚𝐫𝐭𝐞𝐝 𝐀𝐬 ☟︎︎︎ 
 𝐈𝐝 ❥︎ {user.id}
 𝐍𝐚𝐦𝐞 ❥︎ {user.first_name}
 𝐔𝐬𝐞𝐫𝐧𝐚𝐦𝐞 ❥︎ @{user.username}
 ✅✅✅
""")
    except Exception as e:
        await k.edit(f"**ERROR:** `{str(e)}`")
