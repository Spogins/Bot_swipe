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
from aiogram.utils.i18n import gettext as _
from aiogram.utils.i18n import lazy_gettext as __

router = Router()


@router.message(MainMenu.choice, F.text.casefold() == __("advertisements"))
async def show_advertisements(message: Message, state: FSMContext):
    await state.set_state(Advertisement.all)
    advertisements = COLLECTION_ADV.find().sort("date", pymongo.ASCENDING)
    advertisements = [ad for ad in advertisements]
    adv = advertisements[0]

    flat = await get_adv(adv.get('_id'), message.chat.id)

    await message.answer_photo(
        photo=adv.get('scheme'),
        caption=f"{__('Residential Complex')}: {flat.get('residential_complex')['name']}\n"
                f"{__('Section')}: {flat.get('section')['name']}\n"
                f"{__('Corps')}: {flat.get('corps')['name']}\n"
                f"{__('Floor')}: {flat.get('floor')['name']}\n"
                f"{__('Room amount')}: {flat.get('room_amount')}\n"
                f"{__('Price')}: {flat.get('price')}\n"
                f"{__('Square')}: {flat.get('square')}\n"
                f"{__('Kitchen square')}: {flat.get('kitchen')}\n"
                f"{__('Balcony')}: {'Yes' if flat.get('balcony') else 'No'}\n"
                f"{__('Commission')}: {flat.get('commission')}\n"
                f"{__('District')}: {flat.get('district')}\n"
                f"{__('Micro district')}: {flat.get('micro_district')}\n"
                f"{__('Living Condition')}: {flat.get('living_condition')}\n"
                f"{__('Planning')}: {flat.get('planning')}",
        reply_markup=adv_inline_keyboard(adv.get('location'), len(advertisements), 0)
    )

    await message.answer(
        f'Menu',
        reply_markup=to_menu()
    )
