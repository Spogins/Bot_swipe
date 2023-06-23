from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.i18n import gettext as _


def profile_keyboard():
    keywords = ReplyKeyboardMarkup(
                keyboard=[
                    [
                        KeyboardButton(text=_("My Profile")),
                        KeyboardButton(text=_("My Advertisement")),
                    ],
                    [
                        KeyboardButton(text=_("Decline")),
                    ]
                ],
                resize_keyboard=True,
            )
    return keywords


def user_key():
    keywords = ReplyKeyboardMarkup(
                keyboard=[
                    [
                        KeyboardButton(text=_("Main Menu")),
                        KeyboardButton(text=_("Profile Menu")),
                    ],
                ],
                resize_keyboard=True,
            )
    return keywords