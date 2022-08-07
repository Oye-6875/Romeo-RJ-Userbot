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
            if (
               hasattr(imported_module, "__MODULE__")
               and imported_module.__HELP__ 
            ): 
              imported_module.__MODULE__ = imported_module.__MODULE__ 
              if ( 
                hasattr(imported_module, "__HELP__") 
                and imported_module.__HELP__ 
              ):  
               HELPABLE[ 
                   imported_module.__MODULE__.lower()
               ] = imported_module
       console.print(   
           f">> [bold cyan]Successfully imported: [green]{all_module}.py" 
       )  
   console.print("")
   status.update(
     status="[bold blue]Importation Completed!", 
   ) 
  console.print( 
     "[bold green] 🔥 Userbot Started 🔥\n" 
   ) 
  try: 
    await robot.send_message(  
      LOG_GROUP_ID, 
      "<b> 🔥 UserBot is Here 🔥</b>", 
     )
  except Exception as e: 
    print( 
       "\nBot. Has Failed To Access The Log Group, Be Sure You Have Added Your Bot To Your Log Channel And Promoted As Admin❗"
    )
    console.print(f"\n[red] Stopping Bot") 
    return 
  a = await robot.get_chat_member(LOG_GROUP_ID, BOT_ID) 
  if a.status != "administrator": 
    print("Promote Bot As Admin in Logger Group") 
    console.print(f"\n[red]sᴛᴏᴘᴘɪɴɢ ʙᴏᴛ") 
    return 
  console.print(f"\n┌[red] Bot Started as {BOT_NAME}") 
  console.print(f"├[green] ID :- {BOT_ID}") 
  if STRING_SESSION != "None": 
     try: 
        await client.send_message( 
          LOG_GROUP_ID, 
          "<b>🔥 UserBot is Active 🔥</b>", 
        )  
     except Exception as e: 
        print( 
           "\nUserBot Account Has Failed To Access The Log Group.❗" 
        ) 
        console.print(f"\n[red] Stopping Bot") 
        return 
      try: 
        await client.join_chat("All_time_masti_official") 
        await client.join_chat("GirlboyDp143") 
      except: 
        pass 
      console.print(f"├[red] UserBot Started as {ASSNAME}") 
      console.print(f"├[green] ID :- {ASSID}") 
      console.print(f"└[red] ✅  UserBot Boot Complete 💯 ...") 
      await idle()
      console.print(f"\n[red] Userbot Stopped") 
      
      
 home_text_pm = f"""**ʜᴇʟʟᴏ , 
 ᴍʏ ɴᴀᴍᴇ ɪs {BOT_NAME}. 
 I Aᴍ RomeoRJ, Aɴ Aᴅᴠᴀɴᴄᴇᴅ UsᴇʀBᴏᴛ Wɪᴛʜ Sᴏᴍᴇ Usᴇғᴜʟ Fᴇᴀᴛᴜʀᴇs.**"""
 
 
@robot.on_message(command(["start"]) & filters.private) 
async def start(_, message): 
   await message.reply_photo( 
     photo=f"https://telegra.ph/file/627581473dd421c161561.jpg", 
     caption=f"""**━━━━━━━━━━━━━━━━━━━━━━━━ 
🔥 Hᴇʟʟᴏ, I Aᴍ RomeoRJ » Aɴ Aᴅᴠᴀɴᴄᴇᴅ 
Pʀᴇᴍɪᴜᴍ Tᴇʟᴇɢʀᴀᴍ Usᴇʀ Bᴏᴛ. 

┏━━━━━━━━━━━━━━━━━━━┓
┣★ Oᴡɴᴇʀ'xD› : [RomeoRJ](https://t.me/Romeo_RJ_143) 
┣★ Uᴘᴅᴀᴛᴇs ›› : [ ATM ](https://t.me/All_time_masti_official)
┣★ Sᴜᴘᴘᴏʀᴛ » : [DP Channel](https://t.me/GirlboyDp143)
┗━━━━━━━━━━━━━━━━━━━┛ 

💞 Cʟɪᴄᴋ Oɴ Dᴇᴘʟᴏʏ Bᴜᴛᴛᴏɴ Tᴏ Mᴀᴋᴇ 
 Yᴏᴜʀ Oᴡɴ » RomeoRJ Usᴇʀ Bᴏᴛ.  
 ━━━━━━━━━━━━━━━━━━━━━━━━**""", 
     reply_markup=InlineKeyboardMarkup( 
             [ 
                 [ 
                    InlineKeyboardButton( 
                       "💥 Dᴇᴘʟᴏʏ RomeoRJ UsᴇʀBᴏᴛ ✨", url=f"https://github.com/Romeo-RJ-143/Romeo-RJ-Userbot") 
                  ] 
               
             ] 
         ), 
     )
  
  
  
@robot.on_message(command(["help"]) & SUDOERS) 

  
  
  
