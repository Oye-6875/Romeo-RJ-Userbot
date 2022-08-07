import asyncio 
import os 
import time
from os import listdir, mkdir

import heroku3 
from aiohttp import ClientSession 
from git import Repo 
from git.exc import GitCommandError, InvalidGitRepositoryError 
from rich.console import Console 
from rich.table import Table 
from motor.motor_asyncio import AsyncIOMotorClient as KaalXD 

from RomeoRJ.config import MONGO_DB_URL, LOG_GROUP_ID, OWNER_ID, STRING_SESSION, SUDO_USERS, UPSTREAM_BRANCH, UPSTREAM_REPO
from RomeoRJ.modules.clientbot.clientbot import client, robot, pytgcalls 
from RomeoRJ.utilities.misc import sudo 
from RomeoRJ.utilities.times import time_to_seconds 
from RomeoRJ.utilities.tasks import install_requirements 


loop = asyncio.get_event_loop() 
console = Console() 


### Heroku Shit
UPSTREAM_BRANCH = UPSTREAM_BRANCH 
UPSTREAM_REPO = UPSTREAM_REPO 

### Modules
MOD_LOAD = []
MOD_NOLOAD = [] 

### Mongo DB 
MONGODB_CLI = KaalXD(MONGO_DB_URL) 
db = MONGODB_CLI.RomeoRJ

### Sudo Users
sudo()

### Boot Time
boottime = time.time() 

### Clients
aiohttpsession = ClientSession() 
robot = robot 
pytgcalls = pytgcalls

### Config 
SUDOERS = SUDO_USERS 
OWNER_ID = OWNER_ID 
LOG_GROUP_ID = LOG_GROUP_ID 

### Bot Info
BOT_ID = 0 
BOT_NAME = "" 
BOT_USERNAME = "" 

### Assistant Info 
ASSIDS = [] 
ASSID = 0 
ASSNAME = "" 
ASSUSERNAME = "" 
ASSMENTION = "" 
random_assistant = [] 


async def initiate_bot():
    global SUDOERS, OWNER_ID, ASSIDS 
    global BOT_ID, BOT_NAME, BOT_USERNAME 
    global ASSID, ASSNAME, ASSMENTION, ASSUSERNAME 
    global Heroku_cli, Heroku_app 
    os.system("clear") 
    header = Table(show_header=True, header_style="bold yellow") 
    header.add_column( 
        "RomeoRJ Userbot : Best Ever Userbot"
