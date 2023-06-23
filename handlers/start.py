import logging
from aiogram import F, Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.utils.i18n import gettext as _
from aiogram.utils.i18n import lazy_gettext as __
from handlers.main_menu import main_menu
from keyboards.reply.retry import try_or_exit
from keyboards.reply.start import *
from services.user_data import get_user, add_user, update_token, get_new_token
from services.validators import *
from states.main_menu import MainMenu
from states.registration import Register
from states.start import *

# All handlers should be attached to the Router (or Dispatcher)
router = Router()


# initial start command
@router.message(Register.complete, F.text.casefold() == __("decline"))
@router.message(Register.complete, F.text.casefold() == __("go to title"))
@router.message(Register.password, F.text.casefold() == __("decline"))
@router.message(Start.auth, F.text.casefold() == __("decline"))
@router.message(Start.validate, F.text.casefold() == __("decline"))
@router.message(Register.email, F.text.casefold() == __("decline"))
@router.message(Register.validate, F.text.casefold() == __("decline"))
@router.message(Start.start, F.text.casefold() == __("decline"))
@router.message(Register.confirm_password, F.text.casefold() == __("decline"))
@router.message(Register.validate_psw, F.text.casefold() == __("decline"))
@router.message(Command(commands=["start"]))
async def command_start(message: Message, state: FSMContext) -> None:
    await state.clear()
    # set first state
    await state.set_state(Start.start)
    await message.answer(
        _('Nice to meet you!'),
        reply_markup=get_start(),
    )


# entering email
@router.message(Start.auth, F.text.casefold() == __("try again"))
@router.message(Start.auth, F.text.casefold() == __("back"))
@router.message(Start.start, F.text.casefold() == __("try again"))
@router.message(Start.start, F.text.casefold() == __("log in"))
async def log_mail(message: Message, state: FSMContext) -> None:
    await message.answer(
        _("Enter your email."),
        reply_markup=exit_key(),
    )
    # jump to validation email
    await state.set_state(Start.validate)


# validation email and switch on states
@router.message(Start.validate)
async def try_validate(message: Message, state: FSMContext) -> None:
    if is_email(message.text):
        # if valid jump to password entry
        await state.update_data(username=message.text)  # save email from message
        await state.set_state(Start.password)
        await log_psw(message, state)

    else:
        # if not valid, ask the user to try again or cancel to exit
        await message.answer(
            _("You entered is not valid email!"),
            reply_markup=try_or_exit(),
        )
        await state.set_state(Start.start)


@router.message(Start.password)
async def log_psw(message: Message, state: FSMContext) -> None:
    await message.answer(
        _("Enter your password."),
        reply_markup=decline_back()
    )
    await state.set_state(Start.auth)


@router.message(Start.auth)
async def auth(message: Message, state: FSMContext) -> None:
    data = await state.get_data()
    username = data.get('username')  # get user email from saved data
    password = message.text  # Get password from the message
    check = await check_email(username)
    if check:
        token = await auth_check(username, password)
        if token.get('detail'):
            await message.answer(_('Incorrect password'), reply_markup=try_or_exit())
        else:
            await state.set_state(MainMenu.menu)
            usr = await get_user(message.chat.id)
            if not usr:
                data = {
                    'email': data.get('username'),
                    'password': message.text,
                    'access': token["access"],
                    'refresh': token["refresh"]
                }
                await add_user(message.chat.id, data)
            else:
                data = {
                    'access': token["access"],
                    'refresh': token["refresh"]
                }
                await update_token(message.chat.id, data)
            await message.answer(
                f'{_("User have access")}\n',
                # f'User have access\n access: {token["access"]}\n refresh: {token["refresh"]}',
                reply_markup=ReplyKeyboardRemove()
            )
            await main_menu(message, state)
    else:
        await message.answer(
            _('Invalid email!'),
            reply_markup=try_or_exit(),
        )
        await state.set_state(Start.start)


# cancel/exit from seance
# @router.message(Command("cancel"))
# @router.message(F.text.casefold() == "cancel")
@router.message(Exit.cancel, F.text.casefold() == __("decline"))
async def cancel_handler(message: Message, state: FSMContext) -> None:
    current_state = await state.get_state()
    if current_state is None:
        return

    logging.info("Cancelling state %r", current_state)
    await state.clear()
    await message.answer(
        "Cancelled.",
        reply_markup=ReplyKeyboardRemove(),
    )

