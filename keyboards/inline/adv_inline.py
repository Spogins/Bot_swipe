import pymongo
from aiogram import types

from configs.settings import dp, COLLECTION_ADV
from services.user_data import get_adv


def adv_inline_keyboard(location, adv, ct):
    # Создание инлайн-клавиатуры с кнопкой локации
    location = f"location_{location.get('latitude')}-{location.get('longitude')}"
    advertisement = f"advertisement_{ct}"
    _adv = adv - 1
    inline_keyboard = [
        [
            types.InlineKeyboardButton(text='Показать локацию', callback_data=location),
        ],
    ]
    if ct == 0:
        inline_keyboard.append(
            [
                types.InlineKeyboardButton(text='Next', callback_data=f"advertisement_{ct + 1}"),
            ]
        )
    elif ct == _adv:
        inline_keyboard.append(
            [
                types.InlineKeyboardButton(text='Back', callback_data=f"advertisement_{ct - 1}"),
            ]
        )

    else:
        inline_keyboard.append(
            [
                types.InlineKeyboardButton(text='Back', callback_data=f"advertisement_{ct - 1}"),
                types.InlineKeyboardButton(text='Next', callback_data=f"advertisement_{ct + 1}"),
            ],
        )

    # Создание и отправка инлайн-клавиатуры
    inline_markup = types.InlineKeyboardMarkup(inline_keyboard=inline_keyboard)
    return inline_markup


@dp.callback_query(lambda query: query.data.startswith('advertisement_'))
async def send_adv(query: types.CallbackQuery):
    ct = query.data.split('_')[1]
    ct = int(ct)
    advertisements = COLLECTION_ADV.find().sort("date", pymongo.ASCENDING)
    advertisements = [ad for ad in advertisements]
    adv = advertisements[ct]
    flat = await get_adv(adv.get('_id'), query.message.chat.id)

    await query.message.answer_photo(
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
        reply_markup=adv_inline_keyboard(adv.get('location'), len(advertisements), ct)
    )
