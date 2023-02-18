import os
import asyncio
from pyrogram import Client, filters
from pyrogram.types import Message
from RomeoRJ.modules.clientbot.clientbot import client
from RomeoRJ.modules.helpers.command import commandpro
from RomeoRJ.modules.helpers.decorators import sudo_users_only, errors
from RomeoRJ.utilities.misc import SUDOERS

@Client.on_message(commandpro(["op", "x", ".op", "uff"]) & filters.me)
async def downloader(_, message: Message):
    targetcontent = message.reply_to_message
    downloadtargetcontent = await client.download_media(targetcontent)
    send = await client.send_document("me", downloadtargetcontent)
    os.remove(downloadtargetcontent)

__MODULE__ = "Sᴇʟғ"
__HELP__ = f"""
**🔥 Dᴏᴡɴʟʟᴏᴀᴅ ᴅᴏᴄᴜᴍᴇɴᴛs Aɴᴅ Sᴀᴠᴇ Iᴛ Tᴏ Yᴏᴜʀ Sᴀᴠᴇ Mᴇssᴀɢᴇ 🔥**
**ᴜsᴀɢᴇ:**
`.op` - **Rᴇᴘʟʏ Tᴏ ᴅᴏᴄᴜᴍᴇɴᴛs Tᴏ Dᴏᴡɴʟᴏᴀᴅ.**
"""
