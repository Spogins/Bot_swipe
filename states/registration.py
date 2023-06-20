from aiogram.fsm.state import StatesGroup, State


class Register(StatesGroup):
    email = State()
    validate = State()
    validate_psw = State()
    password = State()
    password_equal = State()
    confirm_password = State()
    complete = State()
    complete_reg = State()