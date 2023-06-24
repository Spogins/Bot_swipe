import asyncio
import pymongo
from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from aiogram.utils.i18n import gettext as _
from aiogram.utils.i18n import lazy_gettext as __
from configs.settings import COLLECTION_ADV
from keyboards.inline.show_location import show_location
from keyboards.reply.profile_key import profile_keyboard, user_key
from services.user_data import get_user, get_adv
from states.main_menu import MainMenu
from states.profile_state import Profile

router = Router()


@router.message(Profile.my_adv, F.text.casefold() == __("profile menu"))
@router.message(Profile.profile, F.text.casefold() == __("profile menu"))
@router.message(MainMenu.choice, F.text.casefold() == __("profile"))
async def profile(message: Message, state: FSMContext):
    await state.set_state(Profile.choice)
    await message.answer(
        _("Profile menu"),
        reply_markup=profile_keyboard(),
    )


@router.message(Profile.choice, F.text.casefold() == __("my profile"))
async def user_data(message: Message, state: FSMContext):
    await state.set_state(Profile.profile)
    user = await get_user(message.chat.id)
    await message.answer(
        f"{message.chat.first_name}\n"
        f"{user.get('email')}",
        reply_markup=user_key()
    )


@router.message(Profile.choice, F.text.casefold() == __("my advertisement"))
async def user_adv(message: Message, state: FSMContext):
    await state.set_state(Profile.my_adv)
    advertisements = COLLECTION_ADV.find({'user': message.chat.id}).sort("date", pymongo.ASCENDING)
    advertisements = [ad for ad in advertisements]
    if len(advertisements) != 0:
        for adv in advertisements:
            flat = await get_adv(adv.get('_id'), message.chat.id)
            await message.answer_photo(
                photo=adv.get('scheme'),
                caption=f"{_('Residential Complex')}: {flat.get('residential_complex')['name']}\n"
                        f"{_('Section')}: {flat.get('section')['name']}\n"
                        f"{_('Corps')}: {flat.get('corps')['name']}\n"
                        f"{_('Floor')}: {flat.get('floor')['name']}\n"
                        f"{_('Room amount')}: {flat.get('room_amount')}\n"
                        f"{_('Price')}: {flat.get('price')}\n"
                        f"{_('Square')}: {flat.get('square')}\n"
                        f"{_('Kitchen square')}: {flat.get('kitchen')}\n"
                        f"{_('Balcony')}: {'Yes' if flat.get('balcony') else 'No'}\n"
                        f"{_('Commission')}: {flat.get('commission')}\n"
                        f"{_('District')}: {flat.get('district')}\n"
                        f"{_('Micro district')}: {flat.get('micro_district')}\n"
                        f"{_('Living Condition')}: {flat.get('living_condition')}\n"
                        f"{_('Planning')}: {flat.get('planning')}",
                reply_markup=show_location(adv.get('location'))
            )
            await asyncio.sleep(0.75)
    await message.answer(
        _('Done'),
        reply_markup=user_key()
    )
