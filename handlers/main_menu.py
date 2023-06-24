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
from aiogram.utils.i18n import gettext as _
from aiogram.utils.i18n import lazy_gettext as __
router = Router()


@router.message(Advertisement.all, F.text.casefold() == __("main menu"))
@router.message(Profile.my_adv, F.text.casefold() == __("main menu"))
@router.message(Profile.profile, F.text.casefold() == __("main menu"))
@router.message(Profile.choice, F.text.casefold() == __("decline"))
@router.message(CreateAdvertisement.validate, F.text.casefold() == __("decline"))
@router.message(CreateAdvertisement.corps, F.text.casefold() == __("decline"))
@router.message(CreateAdvertisement.floor, F.text.casefold() == __("decline"))
@router.message(CreateAdvertisement.room_amount, F.text.casefold() == __("decline"))
@router.message(CreateAdvertisement.price, F.text.casefold() == __("decline"))
@router.message(CreateAdvertisement.square, F.text.casefold() == __("decline"))
@router.message(CreateAdvertisement.kitchen_square, F.text.casefold() == __("decline"))
@router.message(CreateAdvertisement.balcony, F.text.casefold() == __("decline"))
@router.message(CreateAdvertisement.commission, F.text.casefold() == __("decline"))
@router.message(CreateAdvertisement.district, F.text.casefold() == __("decline"))
@router.message(CreateAdvertisement.micro_district, F.text.casefold() == __("decline"))
@router.message(CreateAdvertisement.living_condition, F.text.casefold() == __("decline"))
@router.message(CreateAdvertisement.planning, F.text.casefold() == __("decline"))
@router.message(CreateAdvertisement.scheme, F.text.casefold() == __("decline"))
@router.message(CreateAdvertisement.photo_gallery, F.text.casefold() == __("decline"))
@router.message(CreateAdvertisement.location, F.text.casefold() == __("decline"))
@router.message(CreateAdvertisement.check, F.text.casefold() == __("decline"))
@router.message(CreateAdvertisement.section, F.text.casefold() == __("decline"))
@router.message(MainMenu.menu)
async def main_menu(message: Message, state: FSMContext):
    await state.clear()
    await state.set_state(MainMenu.choice)
    await message.answer(
        _("Main menu"),
        reply_markup=main_keyboard(),
    )

# language choose
@router.message(MainMenu.choice, F.text.casefold() == __("language"))
async def lang_choose(message: Message, state: FSMContext) -> None:
    await state.set_state(Start.language)
    await message.answer(
        _("Choose you language!"),
        reply_markup=language(),
    )


@router.message(Start.language, F.text.casefold() == 'русский')
async def lang_rus(message: Message, state: FSMContext) -> None:
    await state.update_data(language='ru')
    await state.set_state(MainMenu.menu)
    await main_menu(message, state)


@router.message(Start.language, F.text.casefold() == 'english')
async def lang_eng(message: Message, state: FSMContext) -> None:
    await state.update_data(language='en')
    await state.set_state(MainMenu.menu)
    await main_menu(message, state)