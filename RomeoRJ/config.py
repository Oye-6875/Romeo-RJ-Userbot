import os 
import aiohttp 
from os import getenv 
from dotenv import load_dotenv 

if os.path.exists("RJ"): 
    load_dotenv("RJ") 
    
aiohttpsession = aiohttp.ClientSession() 
admins = {} 
que = {}

API_ID = int(getenv("API_ID", "13146123"))
API_HASH = getenv("API_HASH", None) 
BOT_TOKEN = getenv("BOT_TOKEN", None)
STRING_SESSION = getenv("STRING_SESSION", None) 
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", ". ! /").split()) 
MONGO_DB_URL = getenv("MONGO_DB_URL", None) 
OWNER_ID = list(map(int, getenv("OWNER_ID", None).split())) 
LOG_GROUP_ID = int(getenv("LOG_GROUP_ID", None)) 
SUDO_USERS = list(map(int, getenv("SUDO_USERS", None).split())) 
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/Romeo-RJ-143/Romeo-RJ-Userbot")
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")
