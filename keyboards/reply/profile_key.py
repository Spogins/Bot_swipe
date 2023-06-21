from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def profile_keyboard():
    keywords = ReplyKeyboardMarkup(
                keyboard=[
                    [
                        KeyboardButton(text="My Profile"),
                        KeyboardButton(text="My Advertisement"),
                    ],
                    [
                        KeyboardButton(text="Decline"),
                    ]
                ],
                resize_keyboard=True,
            )
    return keywords


def user_key():
    keywords = ReplyKeyboardMarkup(
                keyboard=[
                    [
                        KeyboardButton(text="Main Menu"),
                        KeyboardButton(text="Profile Menu"),
                    ],
                ],
                resize_keyboard=True,
            )
    return keywords