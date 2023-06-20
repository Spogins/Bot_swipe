from aiogram.fsm.state import StatesGroup, State


class MainMenu(StatesGroup):
    menu = State()
    choice = State()
    # advertisement = State()
    # create_adv = State()
    # profile = State()