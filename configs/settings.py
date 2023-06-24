# Bot token can be obtained via https://t.me/BotFather
import os
from pathlib import Path
import pymongo
from aiogram import Bot, Dispatcher
from aioredis import Redis
from aiogram.fsm.storage.redis import RedisStorage

TOKEN = "5645187078:AAEPElIJeR5iM-KGvQwJLr_YaRqNoRlVTT8"
API_ROOT = 'http://209.38.231.163'

DB_CLIENT = pymongo.MongoClient("mongodb://localhost:27017/")
CURRENT_DB = DB_CLIENT["swipe"]
COLLECTION = CURRENT_DB["users"]
COLLECTION_ADV = CURRENT_DB["advertisement"]
BOT = Bot(TOKEN, parse_mode="HTML")


BASE_DIR = Path(__file__).resolve().parent.parent
LOCALES_DIR = os.path.join(BASE_DIR, 'locales')

# redis storage
REDIS = Redis()
REDIS_STORAGE = RedisStorage(redis=REDIS)
# Dispatcher is a root router
dp = Dispatcher(storage=REDIS_STORAGE)




