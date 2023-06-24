from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.i18n import gettext as _


def get_start() -> ReplyKeyboardMarkup:
    keyboard = ReplyKeyboardMarkup(
            keyboard=[
                [
                          # switch to choose language
                    KeyboardButton(text=_("Log in")),  # switch to start auth
                    KeyboardButton(text=_("Registration")),  # switch to start auth
                ]
            ],
            resize_keyboard=True,
        )
    return keyboard


def language() -> ReplyKeyboardMarkup:
    keyboard = ReplyKeyboardMarkup(
            keyboard=[
                [
                    KeyboardButton(text="Русский"),
                    KeyboardButton(text="English"),
                ]
            ],
            resize_keyboard=True,
        )
    return keyboard


def decline_back() -> ReplyKeyboardMarkup:
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text=_("Decline")),
                KeyboardButton(text=_("Back")),
            ]
        ],
        resize_keyboard=True,
    )
    return keyboard


def complete_registration() -> ReplyKeyboardMarkup:
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text=_("Change email")),
                KeyboardButton(text=_("Change password")),
                KeyboardButton(text=_("Decline")),
                KeyboardButton(text=_("Complete")),
            ]
        ],
        resize_keyboard=True,
    )
    return keyboard


def exit_key() -> ReplyKeyboardMarkup:
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text=_("Decline")),
            ]
        ],
        resize_keyboard=True,
    )
    return keyboard


def back_key() -> ReplyKeyboardMarkup:
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text=_("Back")),
            ]
        ],
        resize_keyboard=True,
    )
    return keyboard


def to_start() -> ReplyKeyboardMarkup:
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text=_("Go to title")),
            ]
        ],
        resize_keyboard=True,
    )
    return keyboard