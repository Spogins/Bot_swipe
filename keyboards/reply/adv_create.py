from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# draft = ('draft', 'Черновая')
# repair_required = ('repair', 'Нужен ремонт')
# good = ('good', 'В жилом состоянии')
# studio_bathroom = ('studio-bathroom', 'Студия санузел')
#         studio = ('studio', 'Студия')
def conditions_choice() -> ReplyKeyboardMarkup:
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text="draft"),
                KeyboardButton(text="repair"),
                KeyboardButton(text="good"),
                KeyboardButton(text="Decline"),
                KeyboardButton(text="Back"),
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
                KeyboardButton(text="Decline changing"),
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
                KeyboardButton(text="Decline"),
                KeyboardButton(text="Back"),
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
                KeyboardButton(text="Decline changing"),
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
                KeyboardButton(text="Decline"),
                KeyboardButton(text="Back"),
            ]
        ],
        resize_keyboard=True,
    )
    return keyboard


def balcony_changing() -> ReplyKeyboardMarkup:
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text="Yes"),
                KeyboardButton(text="No"),
            ],
            [
                KeyboardButton(text="Decline changing"),
            ]
        ],
        resize_keyboard=True,
    )
    return keyboard


def location_add() -> ReplyKeyboardMarkup:
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text="Add location", request_location=True),
                KeyboardButton(text="Decline"),
                KeyboardButton(text="Back"),
            ]
        ],
        resize_keyboard=True,
    )
    return keyboard


def change_adv() -> ReplyKeyboardMarkup:
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text="Change Residential"),
                KeyboardButton(text="Change Corps"),
                KeyboardButton(text="Change Section"),
            ],
            [
                KeyboardButton(text="Change Floor"),
                KeyboardButton(text="Change Room amount"),
                KeyboardButton(text="Change Price"),
            ],
            [
                KeyboardButton(text="Change Square"),
                KeyboardButton(text="Change Kitchen square"),
                KeyboardButton(text="Change Balcony"),
            ],
            [
                KeyboardButton(text="Change Commission"),
                KeyboardButton(text="Change District"),
                KeyboardButton(text="Change Micro District"),
            ],
            [
                KeyboardButton(text="Change Living condition"),
                KeyboardButton(text="Change Planning"),
                KeyboardButton(text="Change Scheme"),
            ],
            [
                KeyboardButton(text="Change Photo gallery"),
                KeyboardButton(text="Change Location"),
            ],
            [
                KeyboardButton(text="Complete"),
                KeyboardButton(text="Decline"),
            ]

        ],
        resize_keyboard=True,
    )
    return keyboard
