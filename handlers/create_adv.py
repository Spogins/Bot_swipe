from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, ReplyKeyboardRemove
from handlers.main_menu import main_menu
from keyboards.reply.adv_create import *
from keyboards.reply.retry import try_or_exit, decline_changing
from keyboards.reply.start import *
from services.adv_create import adv_request
from services.user_data import get_new_token, get_user, add_adv
from states.create_adv import CreateAdvertisement, ChangeAdv
from states.main_menu import MainMenu
from aiogram.utils.i18n import gettext as _
from aiogram.utils.i18n import lazy_gettext as __
router = Router()


# photo = message.photo[-1]
#     photo = photo.file_id
#     await message.answer_photo(photo)


@router.message(CreateAdvertisement.check, F.text.casefold() == __("change residential"))
@router.message(CreateAdvertisement.corps, F.text.casefold() == __("back"))
@router.message(MainMenu.choice, F.text.casefold() == __("create advertisement"))
async def res_complex(message: Message, state: FSMContext) -> None:
    data = await state.get_data()
    if not data.get('complete'):
        await state.update_data(res_complex=None)
    await state.set_state(CreateAdvertisement.section) if not data.get('complete') else await state.set_state(
        ChangeAdv.res_complex)
    await message.answer(
        _("Select Residential Complex"),
        reply_markup=exit_key() if not data.get('complete') else decline_changing(),
    )


@router.message(ChangeAdv.res_complex, F.text.casefold() != __("decline changing"))
async def change_res_complex(message, state):
    await state.update_data(res_complex=message.text)
    await message.answer(
        _("Residential Complex changed")
    )
    await check(message, state)
    await state.set_state(CreateAdvertisement.check)


@router.message(CreateAdvertisement.check, F.text.casefold() == __("change section"))
@router.message(CreateAdvertisement.floor, F.text.casefold() == __("back"))
@router.message(CreateAdvertisement.section)
async def section(message: Message, state: FSMContext) -> None:
    data = await state.get_data()
    if not data.get('complete'):
        await state.update_data(section=None)
    if not data.get('res_complex'):
        await state.update_data(res_complex=message.text)
    await state.set_state(CreateAdvertisement.corps) if not data.get('complete') else await state.set_state(
        ChangeAdv.section)
    await message.answer(
        _("Select Section"),
        reply_markup=decline_back() if not data.get('complete') else decline_changing(),
    )


@router.message(ChangeAdv.section, F.text.casefold() != __("decline changing"))
async def change_section(message, state):
    await state.update_data(section=message.text)
    await message.answer(
        _("Section changed"),
        reply_markup=ReplyKeyboardRemove(),
    )
    await check(message, state)
    await state.set_state(CreateAdvertisement.check)


@router.message(CreateAdvertisement.check, F.text.casefold() == __("change corps"))
@router.message(CreateAdvertisement.room_amount, F.text.casefold() == __("back"))
@router.message(CreateAdvertisement.corps)
async def corps(message: Message, state: FSMContext) -> None:
    data = await state.get_data()
    if not data.get('complete'):
        await state.update_data(corps=None)
    if not data.get('section'):
        await state.update_data(section=message.text)
    await state.set_state(CreateAdvertisement.floor) if not data.get('complete') else await state.set_state(
        ChangeAdv.corps)
    await message.answer(
        _("Select Corps"),
        reply_markup=decline_back() if not data.get('complete') else decline_changing(),
    )


@router.message(ChangeAdv.corps, F.text.casefold() != __("decline changing"))
async def change_corps(message, state):
    await state.update_data(corps=message.text)
    await message.answer(
        _("Corps changed"),
        reply_markup=ReplyKeyboardRemove(),
    )
    await check(message, state)
    await state.set_state(CreateAdvertisement.check)


@router.message(CreateAdvertisement.check, F.text.casefold() == __("change floor"))
@router.message(CreateAdvertisement.price, F.text.casefold() == __("back"))
@router.message(CreateAdvertisement.floor)
async def floor(message: Message, state: FSMContext) -> None:
    data = await state.get_data()
    if not data.get('complete'):
        await state.update_data(floor=None)
    if not data.get('corps'):
        await state.update_data(corps=message.text)
    await state.set_state(CreateAdvertisement.room_amount) if not data.get('complete') else await state.set_state(
        ChangeAdv.floor)
    await message.answer(
        _("Select Floor"),
        reply_markup=decline_back() if not data.get('complete') else decline_changing(),
    )


@router.message(ChangeAdv.floor, F.text.casefold() != __("decline changing"))
async def change_floor(message, state):
    await state.update_data(floor=message.text)
    await message.answer(
        _("Floor changed"),
        reply_markup=ReplyKeyboardRemove(),
    )
    await check(message, state)
    await state.set_state(CreateAdvertisement.check)


@router.message(CreateAdvertisement.check, F.text.casefold() == __("change room amount"))
@router.message(CreateAdvertisement.square, F.text.casefold() == __("back"))
@router.message(CreateAdvertisement.room_amount)
async def room_amount(message: Message, state: FSMContext) -> None:
    data = await state.get_data()
    if not data.get('complete'):
        await state.update_data(room_amount=None)
    if not data.get('floor'):
        await state.update_data(floor=message.text)
    await state.set_state(CreateAdvertisement.price) if not data.get('complete') else await state.set_state(
        ChangeAdv.room_amount)
    await message.answer(
        _("Select Room amount"),
        reply_markup=decline_back() if not data.get('complete') else decline_changing(),
    )


@router.message(ChangeAdv.room_amount, F.text.casefold() != __("decline changing"))
async def change_room_amount(message, state):
    await state.update_data(room_amount=message.text)
    await message.answer(
        _("Room amount changed"),
        reply_markup=ReplyKeyboardRemove(),
    )
    await check(message, state)
    await state.set_state(CreateAdvertisement.check)


@router.message(CreateAdvertisement.check, F.text.casefold() == __("change price"))
@router.message(CreateAdvertisement.kitchen_square, F.text.casefold() == __("back"))
@router.message(CreateAdvertisement.price)
async def price(message: Message, state: FSMContext) -> None:
    data = await state.get_data()
    if not data.get('complete'):
        await state.update_data(price=None)
    if not data.get('room_amount'):
        await state.update_data(room_amount=message.text)
    await state.set_state(CreateAdvertisement.square) if not data.get('complete') else await state.set_state(
        ChangeAdv.price)
    await message.answer(
        _("Select Price"),
        reply_markup=decline_back() if not data.get('complete') else decline_changing(),
    )


@router.message(ChangeAdv.price, F.text.casefold() != __("decline changing"))
async def change_price(message, state):
    await state.update_data(price=message.text)
    await message.answer(
        _("Price changed"),
        reply_markup=ReplyKeyboardRemove(),
    )
    await check(message, state)
    await state.set_state(CreateAdvertisement.check)


@router.message(CreateAdvertisement.check, F.text.casefold() == __("change square"))
@router.message(CreateAdvertisement.balcony, F.text.casefold() == __("back"))
@router.message(CreateAdvertisement.square)
async def square(message: Message, state: FSMContext) -> None:
    data = await state.get_data()
    if not data.get('complete'):
        await state.update_data(square=None)
    if not data.get('price'):
        await state.update_data(price=message.text)
    await state.set_state(CreateAdvertisement.kitchen_square) if not data.get('complete') else await state.set_state(
        ChangeAdv.square)
    await message.answer(
        _("Select Square"),
        reply_markup=decline_back() if not data.get('complete') else decline_changing(),
    )


@router.message(ChangeAdv.square, F.text.casefold() != __("decline changing"))
async def change_square(message, state):
    await state.update_data(square=message.text)
    await message.answer(
        _("Square changed"),
        reply_markup=ReplyKeyboardRemove(),
    )
    await check(message, state)
    await state.set_state(CreateAdvertisement.check)


@router.message(CreateAdvertisement.check, F.text.casefold() == __("change kitchen square"))
@router.message(CreateAdvertisement.commission, F.text.casefold() == __("back"))
@router.message(CreateAdvertisement.kitchen_square)
async def kitchen_square(message: Message, state: FSMContext) -> None:
    data = await state.get_data()
    if not data.get('complete'):
        await state.update_data(kitchen=None)
    if not data.get('square'):
        await state.update_data(square=message.text)
    await state.set_state(CreateAdvertisement.balcony) if not data.get('complete') else await state.set_state(
        ChangeAdv.kitchen_square)
    await message.answer(
        _("Select Kitchen square"),
        reply_markup=decline_back() if not data.get('complete') else decline_changing(),
    )


@router.message(ChangeAdv.kitchen_square, F.text.casefold() != __("decline changing"))
async def change_kitchen_square(message, state):
    await state.update_data(kitchen=message.text)
    await message.answer(
        _("Kitchen square changed"),
        reply_markup=ReplyKeyboardRemove(),
    )
    await check(message, state)
    await state.set_state(CreateAdvertisement.check)


@router.message(CreateAdvertisement.check, F.text.casefold() == __("change balcony"))
@router.message(CreateAdvertisement.district, F.text.casefold() == __("back"))
@router.message(CreateAdvertisement.balcony)
async def balcony(message: Message, state: FSMContext) -> None:
    data = await state.get_data()
    if not data.get('complete'):
        await state.update_data(balcony=None)
    if not data.get('kitchen'):
        await state.update_data(kitchen=message.text)
    await state.set_state(CreateAdvertisement.commission) if not data.get('complete') else await state.set_state(
        ChangeAdv.balcony)
    await message.answer(
        _("Choice Balcony"),
        reply_markup=balcony_choice() if not data.get('complete') else balcony_changing(),
    )


@router.message(ChangeAdv.balcony, F.text.casefold() != __("decline changing"))
async def change_balcony(message, state):
    _balcony = False
    if message.text.lower() == 'yes':
        _balcony = True
    await state.update_data(balcony=_balcony)
    await message.answer(
        _("Balcony changed"),
        reply_markup=ReplyKeyboardRemove(),
    )
    await check(message, state)
    await state.set_state(CreateAdvertisement.check)


@router.message(CreateAdvertisement.check, F.text.casefold() == __("change commission"))
@router.message(CreateAdvertisement.micro_district, F.text.casefold() == __("back"))
@router.message(CreateAdvertisement.commission)
async def commission(message: Message, state: FSMContext) -> None:
    data = await state.get_data()
    if not data.get('complete'):
        await state.update_data(commission=None)
    if not data.get('balcony'):
        _balcony = False
        if message.text.lower() == 'yes':
            _balcony = True
        await state.update_data(balcony=_balcony)
    await state.set_state(CreateAdvertisement.district) if not data.get('complete') else await state.set_state(
        ChangeAdv.commission)
    await message.answer(
        _("Select Commission"),
        reply_markup=decline_back() if not data.get('complete') else decline_changing(),
    )


@router.message(ChangeAdv.commission, F.text.casefold() != __("decline changing"))
async def change_commission(message, state):
    await state.update_data(commission=message.text)
    await message.answer(
        _("Commission changed"),
        reply_markup=ReplyKeyboardRemove(),
    )
    await check(message, state)
    await state.set_state(CreateAdvertisement.check)


@router.message(CreateAdvertisement.check, F.text.casefold() == __("change district"))
@router.message(CreateAdvertisement.living_condition, F.text.casefold() == __("back"))
@router.message(CreateAdvertisement.district)
async def district(message: Message, state: FSMContext) -> None:
    data = await state.get_data()
    if not data.get('complete'):
        await state.update_data(district=None)
    if not data.get('commission'):
        await state.update_data(commission=message.text)
    await state.set_state(CreateAdvertisement.micro_district) if not data.get('complete') else await state.set_state(
        ChangeAdv.district)
    await message.answer(
        _("Select District"),
        reply_markup=decline_back() if not data.get('complete') else decline_changing(),
    )


@router.message(ChangeAdv.district, F.text.casefold() != __("decline changing"))
async def change_district(message, state):
    await state.update_data(district=message.text)
    await message.answer(
        _("District changed"),
        reply_markup=ReplyKeyboardRemove(),
    )
    await check(message, state)
    await state.set_state(CreateAdvertisement.check)


@router.message(CreateAdvertisement.check, F.text.casefold() == __("change micro district"))
@router.message(CreateAdvertisement.planning, F.text.casefold() == __("back"))
@router.message(CreateAdvertisement.micro_district)
async def micro_district(message: Message, state: FSMContext) -> None:
    data = await state.get_data()
    if not data.get('complete'):
        await state.update_data(micro_district=None)
    if not data.get('district'):
        await state.update_data(district=message.text)
    await state.set_state(CreateAdvertisement.living_condition) if not data.get('complete') else await state.set_state(
        ChangeAdv.micro_district)
    await message.answer(
        _("Select Micro District"),
        reply_markup=decline_back() if not data.get('complete') else decline_changing(),
    )


@router.message(ChangeAdv.micro_district, F.text.casefold() != __("decline changing"))
async def change_micro_district(message, state):
    await state.update_data(micro_district=message.text)
    await message.answer(
        _("Micro district changed"),
        reply_markup=ReplyKeyboardRemove(),
    )
    await check(message, state)
    await state.set_state(CreateAdvertisement.check)


@router.message(CreateAdvertisement.check, F.text.casefold() == __("change living condition"))
@router.message(CreateAdvertisement.scheme, F.text.casefold() == __("back"))
@router.message(CreateAdvertisement.living_condition)
async def living_condition(message: Message, state: FSMContext) -> None:
    data = await state.get_data()
    if not data.get('complete'):
        await state.update_data(living_condition=None)
    if not data.get('micro_district'):
        await state.update_data(micro_district=message.text)
    await state.set_state(CreateAdvertisement.planning) if not data.get('complete') else await state.set_state(
        ChangeAdv.living_condition)
    await message.answer(
        _("Choice Living condition"),
        reply_markup=conditions_choice() if not data.get('complete') else conditions_changing(),
    )


@router.message(ChangeAdv.living_condition, F.text.casefold() != __("decline changing"))
async def change_living_condition(message, state):
    await state.update_data(living_condition=message.text)
    await message.answer(
        _("Living condition changed"),
        reply_markup=ReplyKeyboardRemove(),
    )
    await check(message, state)
    await state.set_state(CreateAdvertisement.check)


@router.message(CreateAdvertisement.check, F.text.casefold() == __("change planning"))
@router.message(CreateAdvertisement.photo_gallery, F.text.casefold() == __("back"))
@router.message(CreateAdvertisement.planning)
async def planning(message: Message, state: FSMContext) -> None:
    data = await state.get_data()
    if not data.get('complete'):
        await state.update_data(planning=None)
    if not data.get('living_condition'):
        await state.update_data(living_condition=message.text)
    await state.set_state(CreateAdvertisement.scheme) if not data.get('complete') else await state.set_state(
        ChangeAdv.planning)
    await message.answer(
        _("Choice Planning"),
        reply_markup=planning_choice() if not data.get('complete') else planning_changing(),
    )


@router.message(ChangeAdv.planning, F.text.casefold() != __("decline changing"))
async def change_planning(message, state):
    await state.update_data(planning=message.text)
    await message.answer(
        _("Planning changed"),
        reply_markup=ReplyKeyboardRemove(),
    )
    await check(message, state)
    await state.set_state(CreateAdvertisement.check)


@router.message(ChangeAdv.try_scheme, F.text.casefold() == __("try again"))
@router.message(CreateAdvertisement.check, F.text.casefold() == __("change scheme"))
@router.message(CreateAdvertisement.photo_gallery, F.text.casefold() == __("try again"))
@router.message(CreateAdvertisement.location, F.text.casefold() == __("back"))
@router.message(CreateAdvertisement.scheme)
async def scheme(message: Message, state: FSMContext) -> None:
    data = await state.get_data()
    if not data.get('complete'):
        await state.update_data(scheme=None)
    if data.get('planning') is None:
        await state.update_data(planning=message.text)
    await state.set_state(CreateAdvertisement.photo_gallery) if not data.get('complete') else await state.set_state(
        ChangeAdv.scheme)
    await message.answer(
        _("Select Scheme"),
        reply_markup=decline_back() if not data.get('complete') else decline_changing(),
    )


@router.message(ChangeAdv.scheme)
async def change_scheme(message, state):
    try:
        photo = message.photo[-1]
        photo = photo.file_id
        await state.update_data(scheme=photo)
        await message.answer(
            _("Scheme changed"),
            reply_markup=ReplyKeyboardRemove(),
        )
        await check(message, state)
        await state.set_state(CreateAdvertisement.check)
    except:
        await state.set_state(ChangeAdv.try_scheme)
        await message.answer(
            _("Please Send image scheme"),
            reply_markup=try_or_exit(),
        )


@router.message(ChangeAdv.try_gallery, F.text.casefold() == __("try again"))
@router.message(CreateAdvertisement.check, F.text.casefold() == __("change photo gallery"))
@router.message(CreateAdvertisement.location, F.text.casefold() == __("try again"))
@router.message(CreateAdvertisement.validate, F.text.casefold() == __("back"))
@router.message(CreateAdvertisement.photo_gallery)
async def photo_gallery(message: Message, state: FSMContext) -> None:
    data = await state.get_data()
    if not data.get('complete'):
        await state.update_data(photo_gallery=None)
    if data.get('scheme') is None:
        try:
            photo = message.photo[-1]
            photo = photo.file_id
            await state.update_data(scheme=photo)
            await state.set_state(CreateAdvertisement.location) if not data.get('complete') else await state.set_state(
                ChangeAdv.photo_gallery)
            await message.answer(
                _("Select Photo gallery"),
                reply_markup=decline_back() if not data.get('complete') else decline_changing(),
            )
        except:
            await state.set_state(CreateAdvertisement.photo_gallery)
            await message.answer(
                _("Please Send image scheme"),
                reply_markup=try_or_exit(),
            )
    else:
        await state.set_state(CreateAdvertisement.location) if not data.get('complete') else await state.set_state(
            ChangeAdv.photo_gallery)
        await message.answer(
            _("Select photo_gallery"),
            reply_markup=decline_back() if not data.get('complete') else decline_changing(),
        )


@router.message(ChangeAdv.photo_gallery)
async def change_photo_gallery(message, state):
    try:
        photos = message.photo[-1]
        photos = photos.file_id
        await state.update_data(photo_gallery=photos)
        await message.answer(
            _("Photo gallery changed"),
            reply_markup=ReplyKeyboardRemove(),
        )
        await check(message, state)
        await state.set_state(CreateAdvertisement.check)
    except:
        await state.set_state(ChangeAdv.try_gallery)
        await message.answer(
            _("Please Send image gallery"),
            reply_markup=try_or_exit(),
        )


@router.message(ChangeAdv.try_location, F.text.casefold() == __("try again"))
@router.message(CreateAdvertisement.check, F.text.casefold() == __("change location"))
@router.message(CreateAdvertisement.validate, F.text.casefold() == __("try again"))
@router.message(CreateAdvertisement.check, F.text.casefold() == __("back"))
@router.message(CreateAdvertisement.location)
async def location(message: Message, state: FSMContext) -> None:
    data = await state.get_data()
    if not data.get('complete'):
        await state.update_data(location=None)
    if data.get('photo_gallery') is None:
        try:
            photos = message.photo[-1]
            photos = photos.file_id
            # print(photos)
            # photos = [photo.file_id for photo in photos]

            await state.update_data(photo_gallery=photos)
            await state.set_state(CreateAdvertisement.validate)
            await message.answer(
                _("Select location"),
                reply_markup=decline_back() if not data.get('complete') else decline_changing(),
            )
        except:
            await state.set_state(CreateAdvertisement.location)
            await message.answer(
                _("Please Send image gallery"),
                reply_markup=try_or_exit(),
            )
    else:
        await state.set_state(CreateAdvertisement.validate) if not data.get('complete') else await state.set_state(
            ChangeAdv.location)
        await message.answer(
            _("Select location"),
            reply_markup=decline_back() if not data.get('complete') else decline_changing(),
        )


@router.message(ChangeAdv.location)
async def change_location(message, state):
    try:
        await state.update_data(
            location={'longitude': message.location.longitude, 'latitude': message.location.latitude})
        await message.answer(
            _("Location changed"),
            reply_markup=ReplyKeyboardRemove(),
        )
        await check(message, state)
        await state.set_state(CreateAdvertisement.check)
    except:
        await state.set_state(ChangeAdv.try_location)
        await message.answer(
            _("Please Select location"),
            reply_markup=try_or_exit(),
        )


@router.message(CreateAdvertisement.validate)
async def validate(message: Message, state: FSMContext) -> None:
    data = await state.get_data()

    if data.get('location') is None:
        try:
            await state.update_data(
                location={'longitude': message.location.longitude, 'latitude': message.location.latitude})
            await state.set_state(CreateAdvertisement.check)
            await check(message, state)
        except:
            await state.set_state(CreateAdvertisement.validate)
            await message.answer(
                _("Please Select location"),
                reply_markup=try_or_exit(),
            )


@router.message(CreateAdvertisement.complete, F.text.casefold() == __("back"))
@router.message(ChangeAdv.try_location, F.text.casefold() == __("decline"))
@router.message(ChangeAdv.try_gallery, F.text.casefold() == __("decline"))
@router.message(ChangeAdv.try_scheme, F.text.casefold() == __("decline"))
@router.message(ChangeAdv.res_complex, F.text.casefold() == __("decline changing"))
@router.message(ChangeAdv.section, F.text.casefold() == __("decline changing"))
@router.message(ChangeAdv.corps, F.text.casefold() == __("decline changing"))
@router.message(ChangeAdv.floor, F.text.casefold() == __("decline changing"))
@router.message(ChangeAdv.room_amount, F.text.casefold() == __("decline changing"))
@router.message(ChangeAdv.price, F.text.casefold() == __("decline changing"))
@router.message(ChangeAdv.square, F.text.casefold() == __("decline changing"))
@router.message(ChangeAdv.kitchen_square, F.text.casefold() == __("decline changing"))
@router.message(ChangeAdv.balcony, F.text.casefold() == __("decline changing"))
@router.message(ChangeAdv.commission, F.text.casefold() == __("decline changing"))
@router.message(ChangeAdv.district, F.text.casefold() == __("decline changing"))
@router.message(ChangeAdv.micro_district, F.text.casefold() == __("decline changing"))
@router.message(ChangeAdv.living_condition, F.text.casefold() == __("decline changing"))
@router.message(ChangeAdv.planning, F.text.casefold() == __("decline changing"))
@router.message(ChangeAdv.scheme, F.text.casefold() == __("decline changing"))
@router.message(ChangeAdv.photo_gallery, F.text.casefold() == __("decline changing"))
@router.message(ChangeAdv.location, F.text.casefold() == __("decline changing"))
@router.message(CreateAdvertisement.check, F.text.casefold() != __("complete"))
async def check(message: Message, state: FSMContext) -> None:
    await state.set_state(CreateAdvertisement.check)
    data = await state.get_data()
    await state.update_data(complete=True)
    await message.answer(
        f"{_('Select check')}\n"
        f"{_('Residential Complex')}: {data.get('res_complex')}\n"
        f"{_('Section')}: {data.get('section')}\n"
        f"{_('Corps')}: {data.get('corps')}\n"
        f"{_('Floor')}: {data.get('floor')}\n"
        f"{_('Room amount')}: {data.get('room_amount')}\n"
        f"{_('Price')}: {data.get('price')}\n"
        f"{_('Square')}: {data.get('square')}\n"
        f"{_('Kitchen square')}: {data.get('kitchen')}\n"
        f"{_('Balcony')}: {'Yes' if data.get('balcony') else 'No'}\n"
        f"{_('Commission')}: {data.get('commission')}\n"
        f"{_('District')}: {data.get('district')}\n"
        f"{_('Micro district')}: {data.get('micro_district')}\n"
        f"{_('Living Condition')}: {data.get('living_condition')}\n"
        f"{_('Planning')}: {data.get('planning')}",
        reply_markup=change_adv(),
    )
    await message.answer_photo(caption=_('Scheme'), photo=data.get('scheme'))
    await message.answer_location(latitude=data.get('location')['latitude'],
                                  longitude=data.get('location')['longitude'])


@router.message(CreateAdvertisement.check, F.text.casefold() == __("complete"))
async def complete(message: Message, state: FSMContext) -> None:
    data = await state.get_data()
    await state.set_state(CreateAdvertisement.complete)
    _json = await adv_request(message.chat.id, data)
    if _json.get('id'):
        await add_adv(message.chat.id, _json.get('id'), data.get('location'), data.get('scheme'))
        await message.answer(
            f"{_('Congratulation, your Advertisement id')}: {_json.get('id')}",
            reply_markup=ReplyKeyboardRemove()
        )
        await state.clear()
        await state.set_state(MainMenu.menu)
        await main_menu(message, state)
    else:
        await message.answer(
            f"Error {_json}",
            reply_markup=ReplyKeyboardRemove()
        )
        await state.set_state(CreateAdvertisement.check)
        await check(message, state)
