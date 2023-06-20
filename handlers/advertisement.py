from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, ReplyKeyboardRemove

from handlers.start import command_start
from keyboards.reply.retry import *
from keyboards.reply.start import *
from services.validators import *
from states.start import *

router = Router()


