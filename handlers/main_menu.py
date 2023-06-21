from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, ReplyKeyboardRemove
from keyboards.reply.main_menu import main_keyboard
from keyboards.reply.retry import *
from keyboards.reply.start import *
from services.validators import *
from states.advertisement import Advertisement
from states.create_adv import CreateAdvertisement
from states.main_menu import MainMenu
from states.profile_state import Profile
from states.start import *

router = Router()


@router.message(Advertisement.all, F.text.casefold() == "main menu")
@router.message(Profile.my_adv, F.text.casefold() == "main menu")
@router.message(Profile.profile, F.text.casefold() == "main menu")
@router.message(Profile.choice, F.text.casefold() == "decline")
@router.message(CreateAdvertisement.validate, F.text.casefold() == "decline")
@router.message(CreateAdvertisement.corps, F.text.casefold() == "decline")
@router.message(CreateAdvertisement.floor, F.text.casefold() == "decline")
@router.message(CreateAdvertisement.room_amount, F.text.casefold() == "decline")
@router.message(CreateAdvertisement.price, F.text.casefold() == "decline")
@router.message(CreateAdvertisement.square, F.text.casefold() == "decline")
@router.message(CreateAdvertisement.kitchen_square, F.text.casefold() == "decline")
@router.message(CreateAdvertisement.balcony, F.text.casefold() == "decline")
@router.message(CreateAdvertisement.commission, F.text.casefold() == "decline")
@router.message(CreateAdvertisement.district, F.text.casefold() == "decline")
@router.message(CreateAdvertisement.micro_district, F.text.casefold() == "decline")
@router.message(CreateAdvertisement.living_condition, F.text.casefold() == "decline")
@router.message(CreateAdvertisement.planning, F.text.casefold() == "decline")
@router.message(CreateAdvertisement.scheme, F.text.casefold() == "decline")
@router.message(CreateAdvertisement.photo_gallery, F.text.casefold() == "decline")
@router.message(CreateAdvertisement.location, F.text.casefold() == "decline")
@router.message(CreateAdvertisement.check, F.text.casefold() == "decline")
@router.message(CreateAdvertisement.section, F.text.casefold() == "decline")
@router.message(MainMenu.menu)
async def main_menu(message: Message, state: FSMContext):
    await state.clear()
    await state.set_state(MainMenu.choice)
    await message.answer(
        f"Main menu",
        reply_markup=main_keyboard(),
    )
