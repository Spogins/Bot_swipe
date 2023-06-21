from aiogram import types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from configs.settings import BOT, dp


def show_location(location):
    # Создание инлайн-клавиатуры с кнопкой локации
    location = f"location_{location.get('latitude')}-{location.get('longitude')}"
    inline_keyboard = [
        [
            types.InlineKeyboardButton(text='Показать локацию', callback_data=location)
        ]
    ]

    # Создание и отправка инлайн-клавиатуры
    inline_markup = types.InlineKeyboardMarkup(inline_keyboard=inline_keyboard)
    return inline_markup


# Обработчик нажатия на инлайн-кнопку
@dp.callback_query(lambda query: query.data.startswith('location_'))
async def send_location(query: types.CallbackQuery):
    location_data = query.data.split('_')[1]
    latitude, longitude = location_data.split('-')
    # Отправка сообщения с локацией
    await query.message.reply_location(latitude=float(latitude), longitude=float(longitude))