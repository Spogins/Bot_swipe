# Bot token can be obtained via https://t.me/BotFather
import os
import environ
from pathlib import Path
import pymongo
from aiogram import Bot, Dispatcher
from aioredis import Redis
from aiogram.fsm.storage.redis import RedisStorage

env = environ.Env()
environ.Env.read_env(env.str('ENV_PATH', '.env'))


TOKEN = env('TOKEN')
API_ROOT = env('API_ROOT')

DB_CLIENT = pymongo.MongoClient(env('DB_CLIENT'))
CURRENT_DB = DB_CLIENT[env('CURRENT_DB')]
COLLECTION = CURRENT_DB[env('COLLECTION')]
COLLECTION_ADV = CURRENT_DB[env('COLLECTION_ADV')]
BOT = Bot(TOKEN, parse_mode="HTML")


BASE_DIR = Path(__file__).resolve().parent.parent
LOCALES_DIR = os.path.join(BASE_DIR, 'locales')

# redis storage
REDIS = Redis(host='redis', decode_responses=True)
REDIS_STORAGE = RedisStorage(redis=REDIS)
# Dispatcher is a root router
dp = Dispatcher(storage=REDIS_STORAGE)




