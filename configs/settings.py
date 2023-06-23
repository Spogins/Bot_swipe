# Bot token can be obtained via https://t.me/BotFather
import pymongo
from aiogram import Bot, Dispatcher
from aiogram.utils.i18n import I18n, ConstI18nMiddleware
from aioredis import Redis
from aiogram.fsm.storage.redis import RedisStorage

TOKEN = "5645187078:AAEPElIJeR5iM-KGvQwJLr_YaRqNoRlVTT8"
API_ROOT = 'http://209.38.231.163'

DB_CLIENT = pymongo.MongoClient("mongodb://localhost:27017/")
CURRENT_DB = DB_CLIENT["swipe"]
COLLECTION = CURRENT_DB["users"]
COLLECTION_ADV = CURRENT_DB["advertisement"]
BOT = Bot(TOKEN, parse_mode="HTML")


# redis storage
redis = Redis()
storage = RedisStorage(redis=redis)
# Dispatcher is a root router
dp = Dispatcher(storage=storage)

i18n = I18n(path='locales', default_locale='en')
i18n_middleware = ConstI18nMiddleware(i18n=i18n, locale='en')



