from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.i18n import gettext as _


def main_keyboard():
    keywords = ReplyKeyboardMarkup(
                keyboard=[
                    [
                        KeyboardButton(text=_("Advertisements")),
                        KeyboardButton(text=_("Create Advertisement")),
                        KeyboardButton(text=_("Profile")),
                        KeyboardButton(text=_("Language")),
                    ]
                ],
                resize_keyboard=True,
            )
    return keywords


def to_menu():
    keywords = ReplyKeyboardMarkup(
                keyboard=[
                    [
                        KeyboardButton(text=_("Main Menu")),
                    ],
                ],
                resize_keyboard=True,
            )
    return keywords