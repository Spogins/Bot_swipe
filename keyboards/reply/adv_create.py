from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.i18n import gettext as _


def conditions_choice() -> ReplyKeyboardMarkup:
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text="draft"),
                KeyboardButton(text="repair"),
                KeyboardButton(text="good"),
                KeyboardButton(text=_("Decline")),
                KeyboardButton(text=_("Back")),
            ]
        ],
        resize_keyboard=True,
    )
    return keyboard


def conditions_changing() -> ReplyKeyboardMarkup:
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text="draft"),
                KeyboardButton(text="repair"),
                KeyboardButton(text="good"),
            ],
            [
                KeyboardButton(text=_("Decline changing")),
            ]
        ],
        resize_keyboard=True,
    )
    return keyboard


def planning_choice() -> ReplyKeyboardMarkup:
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text="studio"),
                KeyboardButton(text="studio-bathroom"),
                KeyboardButton(text=_("Decline")),
                KeyboardButton(text=_("Back")),
            ]
        ],
        resize_keyboard=True,
    )
    return keyboard


def planning_changing() -> ReplyKeyboardMarkup:
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text="studio"),
                KeyboardButton(text="studio-bathroom"),
            ],
            [
                KeyboardButton(text=_("Decline changing")),
            ]
        ],
        resize_keyboard=True,
    )
    return keyboard


def balcony_choice() -> ReplyKeyboardMarkup:
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text="Yes"),
                KeyboardButton(text="No"),
                KeyboardButton(text=_("Decline")),
                KeyboardButton(text=_("Back")),
            ]
        ],
        resize_keyboard=True,
    )
    return keyboard


def balcony_changing() -> ReplyKeyboardMarkup:
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text=_("Yes")),
                KeyboardButton(text=_("No")),
            ],
            [
                KeyboardButton(text=_("Decline changing")),
            ]
        ],
        resize_keyboard=True,
    )
    return keyboard


def location_add() -> ReplyKeyboardMarkup:
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text=_("Add location"), request_location=True),
                KeyboardButton(text=_("Decline")),
                KeyboardButton(text=_("Back")),
            ]
        ],
        resize_keyboard=True,
    )
    return keyboard


def change_adv() -> ReplyKeyboardMarkup:
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text=_("Change Residential")),
                KeyboardButton(text=_("Change Corps")),
                KeyboardButton(text=_("Change Section")),
            ],
            [
                KeyboardButton(text=_("Change Floor")),
                KeyboardButton(text=_("Change Room amount")),
                KeyboardButton(text=_("Change Price")),
            ],
            [
                KeyboardButton(text=_("Change Square")),
                KeyboardButton(text=_("Change Kitchen square")),
                KeyboardButton(text=_("Change Balcony")),
            ],
            [
                KeyboardButton(text=_("Change Commission")),
                KeyboardButton(text=_("Change District")),
                KeyboardButton(text=_("Change Micro District")),
            ],
            [
                KeyboardButton(text=_("Change Living condition")),
                KeyboardButton(text=_("Change Planning")),
                KeyboardButton(text=_("Change Scheme")),
            ],
            [
                KeyboardButton(text=_("Change Photo gallery")),
                KeyboardButton(text=_("Change Location")),
            ],
            [
                KeyboardButton(text=_("Complete")),
                KeyboardButton(text=_("Decline")),
            ]

        ],
        resize_keyboard=True,
    )
    return keyboard
