from aiogram.fsm.state import StatesGroup, State


class Start(StatesGroup):
    init = State()
    start = State()
    validate = State()
    auth = State()
    password = State()
    language = State()



class Exit(StatesGroup):
    cancel = State()


# class Authorization(StatesGroup):
#     email = State()
#     password = State()


# class Validator(StatesGroup):
#     not_valid = State()
