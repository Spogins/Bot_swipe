from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def main_keyboard():
    keywords = ReplyKeyboardMarkup(
                keyboard=[
                    [
                        KeyboardButton(text="Advertisements"),
                        KeyboardButton(text="Create Advertisement"),
                        KeyboardButton(text="Profile"),
                    ]
                ],
                resize_keyboard=True,
            )
    return keywords