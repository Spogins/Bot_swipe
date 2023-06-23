from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.utils.i18n import gettext as _
from aiogram.utils.i18n import lazy_gettext as __
from handlers.start import command_start
from keyboards.reply.retry import *
from keyboards.reply.start import *
from services.validators import *
from states.registration import Register
from states.start import *

router = Router()


@router.message(Register.complete, F.text.casefold() == __("change email"))
@router.message(Register.email, F.text.casefold() == __("try again"))
@router.message(Register.validate_psw, F.text.casefold() == __("back"))
@router.message(Register.email)
@router.message(Start.start, F.text.casefold() == __("registration"))
async def log_mail(message: Message, state: FSMContext) -> None:
    await message.answer(
        _("Enter your email"),
        reply_markup=exit_key()
    )

    await state.set_state(Register.validate)


@router.message(Register.validate)
async def try_validate(message: Message, state: FSMContext) -> None:
    data = await state.get_data()

    if is_email(message.text):
        check = await check_email(message.text)
        if not check:
            await state.update_data(username=message.text)  # save email from message
            if not data.get('complete'):
                await state.set_state(Register.password)
                await psw(message, state)
            else:
                await state.set_state(Register.complete)
                await complete(message, state)
        else:
            await message.answer(
                _("Mail already in use!"),
                reply_markup=try_or_exit(),
            )
            await state.set_state(Register.email)
    else:
        # if not valid, ask the user to try again or cancel to exit
        await message.answer(
            _("You entered is not valid email!"),
            reply_markup=try_or_exit(),
        )
        await state.set_state(Register.email)


@router.message(Register.complete, F.text.casefold() == __("change password"))
@router.message(Register.password_equal, F.text.casefold() == __("back"))
@router.message(Register.password, F.text.casefold() == __("try again"))
@router.message(Register.password)
async def psw(message: Message, state: FSMContext) -> None:
    data = await state.get_data()
    await message.answer(
        _("Enter your password."),
        reply_markup=decline_back() if not data.get('complete') else ReplyKeyboardRemove()
    )
    await state.set_state(Register.validate_psw)


@router.message(Register.validate_psw)
async def validate_psw(message: Message, state: FSMContext) -> None:
    check = password_check(message.text)
    if check:
        await message.answer(
            text=check,
            reply_markup=try_or_exit()
        )
        await state.set_state(Register.password)
    else:
        await state.set_state(Register.confirm_password)
        await conf_psw(message, state)


@router.message(Register.confirm_password)
async def conf_psw(message: Message, state: FSMContext) -> None:
    data = await state.get_data()
    await message.answer(
        _("Confirm your password."),
        reply_markup=decline_back() if not data.get('complete') else back_key()
    )
    await state.update_data(password=message.text)
    await state.set_state(Register.password_equal)


@router.message(Register.password_equal)
async def equal_psw(message: Message, state: FSMContext) -> None:
    data = await state.get_data()
    if message.text == data['password']:
        await complete(message, state)
        await state.set_state(Register.complete)
    else:
        await message.answer(
            _("Password miss match"),
            reply_markup=try_or_exit()
        )
        await state.set_state(Register.password)


@router.message(Register.complete, F.text.casefold() != __("complete"))
async def complete(message: Message, state: FSMContext) -> None:
    data = await state.get_data()
    await state.update_data(complete=True)
    await message.answer(
        f'{_("Confirm your entry data")}\n'
        f'{_("Email")}: {data["username"]}\n'
        f'{_("Password")}: {data["password"]}',
        reply_markup=complete_registration()
    )


@router.message(Register.complete, F.text.casefold() == __("complete"))
async def complete_reg(message: Message, state: FSMContext) -> None:
    data = await state.get_data()
    response = await registration(data=data)
    if response.get('detail') == 'Verification e-mail sent.':
        await message.answer(
            _('Well done, u have message receipt to your emeil, please check your email inbox and follow instructions to complete registrations'),
            reply_markup=to_start()
        )
    else:
        await message.answer(
            _('Something goes wrong'),
            reply_markup=ReplyKeyboardRemove()
        )
        await command_start(message, state)
