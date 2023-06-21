import asyncio

import pymongo
from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from configs.settings import COLLECTION_ADV
from keyboards.inline.show_location import show_location
from keyboards.reply.profile_key import profile_keyboard, user_key
from services.user_data import get_user, get_adv
from states.main_menu import MainMenu
from states.profile_state import Profile

router = Router()


@router.message(Profile.my_adv, F.text.casefold() == "profile menu")
@router.message(Profile.profile, F.text.casefold() == "profile menu")
@router.message(MainMenu.choice, F.text.casefold() == "profile")
async def profile(message: Message, state: FSMContext):
    await state.set_state(Profile.choice)
    await message.answer(
        f"Profile menu",
        reply_markup=profile_keyboard(),
    )


@router.message(Profile.choice, F.text.casefold() == "my profile")
async def user_data(message: Message, state: FSMContext):
    await state.set_state(Profile.profile)
    user = await get_user(message.chat.id)
    await message.answer(
        f"{message.chat.first_name}\n"
        f"{user.get('email')}",
        reply_markup=user_key()
    )


@router.message(Profile.choice, F.text.casefold() == "my advertisement")
async def user_adv(message: Message, state: FSMContext):
    await state.set_state(Profile.my_adv)
    advertisements = COLLECTION_ADV.find({'user': message.chat.id}).sort("date", pymongo.ASCENDING)
    advertisements = [ad for ad in advertisements]
    if len(advertisements) != 0:
        for adv in advertisements:
            flat = await get_adv(adv.get('_id'), message.chat.id)
            print(flat)
            await message.answer_photo(
                photo=adv.get('scheme'),
                caption=f"Residential Complex: {flat.get('residential_complex')['name']}\n"
                        f"Section: {flat.get('section')['name']}\n"
                        f"Corps: {flat.get('corps')['name']}\n"
                        f"Floor: {flat.get('floor')['name']}\n"
                        f"Room amount: {flat.get('room_amount')}\n"
                        f"Price: {flat.get('price')}\n"
                        f"Square: {flat.get('square')}\n"
                        f"Kitchen square: {flat.get('kitchen')}\n"
                        f"Balcony: {'Yes' if flat.get('balcony') else 'No'}\n"
                        f"Commission: {flat.get('commission')}\n"
                        f"District: {flat.get('district')}\n"
                        f"Micro district {flat.get('micro_district')}\n"
                        f"Living Condition: {flat.get('living_condition')}\n"
                        f"Planning: {flat.get('planning')}",
                reply_markup=show_location(adv.get('location'))
            )
            await asyncio.sleep(0.75)
    await message.answer(
        f'Done',
        reply_markup=user_key()
    )
