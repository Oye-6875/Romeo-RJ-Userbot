# RomeoRJ

import asyncio

from pyrogram import *

from pyrogram.types import *

from RomeoRJ.modules.helpers.basics import edit_or_reply

from RomeoRJ.modules.helpers.filters import command

from RomeoRJ.utilities.misc import SUDOERS

@Client.on_message(command(["alive"]) & SUDOERS)

async def mother_chod(client: Client, message: Message):

    await edit_or_reply(message, "**I'm alive Romeo_RJ**")

__MODULE__ = "Aʟɪᴠᴇ"

__HELP__ = f"""

**🔥 Tᴇsᴛ Yᴏᴜʀ Bᴏᴛ Wᴏʀᴋɪɴɢ Oʀ Nᴏᴛ.**

`.alive` - **Usᴇ Tʜɪs Cᴏᴍᴍᴀɴᴅ Tᴏ Cʜᴇᴄᴋ**

"""
