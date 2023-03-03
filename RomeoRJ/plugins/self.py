import os
import asyncio
from pyrogram import Client, filters
from pyrogram.types import Message
from RomeoRJ.modules.clientbot.clientbot import client
from RomeoRJ.modules.helpers.command import commandpro
from RomeoRJ.modules.helpers.decorators import sudo_users_only, errors
from RomeoRJ.utilities.misc import SUDOERS

@Client.on_message(commandpro([".op", ".x", ".op", ".uff"]) & filters.me)
async def downloader(_, message: Message):
    await message.delete()
    r = message.reply_to_message
    j = await client.download_media(r)
    send = await client.send_document("me", j)
    os.remove(j)

