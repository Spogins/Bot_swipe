# Bot token can be obtained via https://t.me/BotFather
import pymongo
from aiogram import Bot

TOKEN = "5645187078:AAEPElIJeR5iM-KGvQwJLr_YaRqNoRlVTT8"
API_ROOT = 'http://209.38.231.163'

DB_CLIENT = pymongo.MongoClient("mongodb://localhost:27017/")
CURRENT_DB = DB_CLIENT["swipe"]
COLLECTION = CURRENT_DB["users"]
COLLECTION_ADV = CURRENT_DB["advertisement"]
BOT = Bot(TOKEN, parse_mode="HTML")