from aiogram.fsm.state import StatesGroup, State


class MainMenu(StatesGroup):
    menu = State()
    choice = State()
