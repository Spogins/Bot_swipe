from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def get_start() -> ReplyKeyboardMarkup:
    keyboard = ReplyKeyboardMarkup(
            keyboard=[
                [
                    KeyboardButton(text="Language"),  # switch to choose language
                    KeyboardButton(text="Log in"),  # switch to start auth
                    KeyboardButton(text="Registration"),  # switch to start auth
                ]
            ],
            resize_keyboard=True,
        )
    return keyboard


def language() -> ReplyKeyboardMarkup:
    keyboard = ReplyKeyboardMarkup(
            keyboard=[
                [
                    KeyboardButton(text="Rus"),
                    KeyboardButton(text="Eng"),
                ]
            ],
            resize_keyboard=True,
        )
    return keyboard


def decline_back() -> ReplyKeyboardMarkup:
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text="Decline"),
                KeyboardButton(text="Back"),
            ]
        ],
        resize_keyboard=True,
    )
    return keyboard


def complete_registration() -> ReplyKeyboardMarkup:
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text="Change email"),
                KeyboardButton(text="Change password"),
                KeyboardButton(text="Decline"),
                KeyboardButton(text="Complete"),
            ]
        ],
        resize_keyboard=True,
    )
    return keyboard


def exit_key() -> ReplyKeyboardMarkup:
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text="Decline"),
            ]
        ],
        resize_keyboard=True,
    )
    return keyboard


def back_key() -> ReplyKeyboardMarkup:
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text="Back"),
            ]
        ],
        resize_keyboard=True,
    )
    return keyboard


def to_start() -> ReplyKeyboardMarkup:
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text="Go to title"),
            ]
        ],
        resize_keyboard=True,
    )
    return keyboard