from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.i18n import gettext as _


def try_or_exit():
    keywords = ReplyKeyboardMarkup(
                keyboard=[
                    [
                        KeyboardButton(text=_("Try again")),
                        KeyboardButton(text=_("Decline")),
                    ]
                ],
                resize_keyboard=True,
            )
    return keywords


def decline_changing():
    keywords = ReplyKeyboardMarkup(
                keyboard=[
                    [
                        KeyboardButton(text=_("Decline changing")),
                    ]
                ],
                resize_keyboard=True,
            )
    return keywords