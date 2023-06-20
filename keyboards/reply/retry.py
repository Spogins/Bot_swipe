from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def try_or_exit():
    keywords = ReplyKeyboardMarkup(
                keyboard=[
                    [
                        KeyboardButton(text="Try again"),
                        KeyboardButton(text="Decline"),
                    ]
                ],
                resize_keyboard=True,
            )
    return keywords


def decline_changing():
    keywords = ReplyKeyboardMarkup(
                keyboard=[
                    [
                        KeyboardButton(text="Decline changing"),
                    ]
                ],
                resize_keyboard=True,
            )
    return keywords