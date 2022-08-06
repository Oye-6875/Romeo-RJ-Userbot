import asyncio 
import importlib
import os 
import re

from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from pytgcalls import idle
from rich.console import Console
from rich.table import Table
from youtubesearchpython import VideosSearch 

from RomeoRJ.config import LOG_GROUP_ID, STRING_SESSION 
from RomeoRJ import client, robot, pytgcalls, ASSID, ASSNAME, BOT_ID, BOT_NAME, OWNER_ID 
from RomeoRJ.modules.helpers.filters import command
from RomeoRJ.modules.helpers.decorators import errors, sudo_users_only
from RomeoRJ.plugins import ALL_MODULES 
from RomeoRJ.utilities.inline import paginate_modules 
from RomeoRJ.utilities.misc import SUDOERS 

loop = asyncio.get_event_loop() 
console = Console() 
HELPABLE = {}


async def initiate_bot(): 
  with console.status( 
      "[magenta] Finalizing Booting...", 
    ) as status:
        status.update( 
            status="[bold blue]Scanning for Plugins", spinner="earth"
        )
        console.print("Found {} Plugins".format(len(ALL_MODULES)) + "\n")
        status.update(
            status="[bold red]Importing Plugins...", 
            spinner="bouncingBall", 
            spinner_style="yellow", 
          )
        for all_module in ALL_MODULES:
            imported_module = importlib.import_module( 
                "RomeoRJ.plugins." + all_module 
            ) 
            
              
              
              
              
