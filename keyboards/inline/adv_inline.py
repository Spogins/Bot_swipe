import pymongo
from aiogram import types
from aiogram.utils.i18n import gettext as _
from configs.settings import dp, COLLECTION_ADV
from services.user_data import get_adv


def adv_inline_keyboard(location, adv, ct):
    # Создание инлайн-клавиатуры с кнопкой локации
    location = f"location_{location.get('latitude')}-{location.get('longitude')}"
    advertisement = f"advertisement_{ct}"
    _adv = adv - 1
    inline_keyboard = [
        [
            types.InlineKeyboardButton(text=_('Show location'), callback_data=location),
        ],
    ]
    if ct == 0:
        inline_keyboard.append(
            [
                types.InlineKeyboardButton(text=_('Next'), callback_data=f"advertisement_{ct + 1}"),
            ]
        )
    elif ct == _adv:
        inline_keyboard.append(
            [
                types.InlineKeyboardButton(text=_('Back'), callback_data=f"advertisement_{ct - 1}"),
            ]
        )

    else:
        inline_keyboard.append(
            [
                types.InlineKeyboardButton(text=_('Back'), callback_data=f"advertisement_{ct - 1}"),
                types.InlineKeyboardButton(text=_('Next'), callback_data=f"advertisement_{ct + 1}"),
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
    new_photo = adv.get('scheme')
    new_media = types.InputMediaPhoto(media=new_photo)

    await query.message.edit_media(
        media=new_media
    )

    await query.message.edit_caption(
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
        reply_markup=adv_inline_keyboard(adv.get('location'), len(advertisements), ct)
    )

