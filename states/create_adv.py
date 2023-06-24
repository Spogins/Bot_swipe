from aiogram.fsm.state import StatesGroup, State


class CreateAdvertisement(StatesGroup):
    section = State()
    corps = State()
    floor = State()
    room_amount = State()
    price = State()
    square = State()
    kitchen_square = State()
    balcony = State()
    commission = State()
    district = State()
    micro_district = State()
    living_condition = State()
    planning = State()
    scheme = State()
    photo_gallery = State()
    location = State()
    validate = State()
    check = State()
    complete = State()
    gal_validate = State()


class ChangeAdv(StatesGroup):
    res_complex = State()
    section = State()
    corps = State()
    floor = State()
    room_amount = State()
    price = State()
    square = State()
    kitchen_square = State()
    balcony = State()
    commission = State()
    district = State()
    micro_district = State()
    living_condition = State()
    planning = State()
    scheme = State()
    photo_gallery = State()
    location = State()
    try_scheme = State()
    try_gallery = State()
    try_location = State()
    # "scheme": "string",
  # "photo_gallery": [
  #   {
  #     "image": "string"
  #   }
  # ],

