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



