import requests
from datetime import datetime
from pyrogram import filters, Client
from RomeoRJ.utilities.misc import SUDOERS

@Client.on_message(filters.command(["ping"], ["/", ".", "!"]) & SUDOERS)
async def ping(Client, message):
    start = datetime.now()
    loda = await message.reply_text("**Romeo_RJ**")
    end = datetime.now()
    mp = (end - start).microseconds / 1000
    await loda.edit_text(f"**😎 Poɴɢ\n»** `{mp} ms`")

__MODULE__ = "Pɪɴɢ"
__HELP__ = f"""
**🔥 Cʜᴇᴄᴋ Yᴏᴜʀ  UsᴇʀBᴏᴛ Pɪɴɢ.**
`.ping` - **Usᴇ Tʜɪs Cᴏᴍᴍᴀɴᴅ Tᴏ Cʜᴇᴄᴋ**
"""
