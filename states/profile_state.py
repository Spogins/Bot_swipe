from aiogram.fsm.state import StatesGroup, State


class Profile(StatesGroup):
    choice = State()
    profile = State()
    my_adv = State()