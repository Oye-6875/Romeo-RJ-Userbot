from motor.motor_asyncio import AsyncIOMotorClient as _mongo_client_

from pymongo import MongoClient

from pyrogram import Client

from RomeoRJ import config

from ..logger import LOGGER

_mongo_async_ = _mongo_client_(config.MONGO_DB_URL)

_mongo_sync_ = MongoClient(config.MONGO_DB_URL)

mongodb = _mongo_async_.Mongo

pymongodb = _mongo_sync_.Mongo

dbb = _mongo_async_["ROMEORJDB"]
