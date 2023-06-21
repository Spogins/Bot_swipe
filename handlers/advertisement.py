import pymongo
from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from configs.settings import COLLECTION_ADV
from keyboards.inline.adv_inline import adv_inline_keyboard
from keyboards.inline.show_location import show_location
from keyboards.reply.main_menu import to_menu
from services.user_data import get_adv
from states.advertisement import Advertisement
from states.main_menu import MainMenu


router = Router()


@router.message(MainMenu.choice, F.text.casefold() == "advertisements")
async def show_advertisements(message: Message, state: FSMContext):
    await state.set_state(Advertisement.all)
    advertisements = COLLECTION_ADV.find().sort("date", pymongo.ASCENDING)
    advertisements = [ad for ad in advertisements]
    print(advertisements)
    adv = advertisements[0]

    flat = await get_adv(adv.get('_id'), message.chat.id)

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
        reply_markup=adv_inline_keyboard(adv.get('location'), len(advertisements), 0)
    )

    await message.answer(
        f'Done',
        reply_markup=to_menu()
    )