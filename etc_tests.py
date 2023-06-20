# @router.message(Command(commands=["start"]))
# async def command_start_handler(message: Message) -> None:
#     """
#     This handler receive messages with `/start` command
#     """
#     # Most event objects have aliases for API methods that can be called in events' context
#     # For example if you want to answer to incoming message you can use `message.answer(...)` alias
#     # and the target chat will be passed to :ref:`aiogram.methods.send_message.SendMessage`
#     # method automatically or call API method directly via
#     # Bot instance: `bot.send_message(chat_id=message.chat.id, ...)`
#     async def fetch(session, url, headers=None):
#         async with async_timeout.timeout(10):
#             async with session.get(url, headers=headers) as response:
#                 return await response.json()
#
#
#     async with aiohttp.ClientSession() as session:
#         async with session.post('http://209.38.231.163/api/token/', data={'username': 'admin@admin.com', 'password': 'swipe5231'}) as response:
#             token = await response.json()
#             print(token['access'])
#             response = await fetch(
#                 session,
#                 'http://209.38.231.163/api/v1/flat/',
#                 headers={
#                     'Authorization': f'Bearer {token["access"]}'})
#             print(response)
#
#     await message.answer(f"Hello, <b>{message.from_user.full_name}!</b>")


# @router.message()
# async def echo_handler(message: types.Message) -> None:
#     """
#     Handler will forward received message back to the sender
#
#     By default, message handler will handle all message types (like text, photo, sticker and etc.)
#     """
#     try:
#         # Send copy of the received message
#         await message.send_copy(chat_id=message.chat.id)
#     except TypeError:
#         # But not all the types is supported to be copied so need to handle it
#         await message.answer("Nice try!")

#
# @router.message(Command(commands=["start"]))
# async def command_start(message: Message, state: FSMContext) -> None:
#     await state.set_state(Start.name)
#     await message.answer(
#         "Hi there! What's your name?",
#         reply_markup=ReplyKeyboardRemove(),
#     )
#
# @router.message(Start.name)
# async def process_name(message: Message, state: FSMContext) -> None:
#     await state.update_data(name=message.text)
#     await state.set_state(Start.like_bots)
#     await message.answer(
#         f"Nice to meet you, {html.quote(message.text)}!\nDid you like to write bots?",
#         reply_markup=ReplyKeyboardMarkup(
#             keyboard=[
#                 [
#                     KeyboardButton(text="Yes"),
#                     KeyboardButton(text="No"),
#                 ]
#             ],
#             resize_keyboard=True,
#         ),
#     )
#
# @router.message(Start.like_bots, F.text.casefold() == "yes")
# async def process_like_write_bots(message: Message, state: FSMContext) -> None:
#     await state.set_state(Start.language)
#
#     await message.reply(
#         "Cool! I'm too!\nWhat programming language did you use for it?",
#         reply_markup=ReplyKeyboardRemove(),
#     )
#
#
# @router.message(Start.like_bots, F.text.casefold() == "no")
# async def process_dont_like_write_bots(message: Message, state: FSMContext) -> None:
#     data = await state.get_data()
#     await state.clear()
#     await message.answer(
#         "Not bad not terrible.\nSee you soon.",
#         reply_markup=ReplyKeyboardRemove(),
#     )
#     await show_summary(message=message, data=data, positive=False)
#
#
# @router.message(Start.like_bots)
# async def process_unknown_write_bots(message: Message, state: FSMContext) -> None:
#     await message.reply("I don't understand you :(")
#
#
# @router.message(Start.language)
# async def process_language(message: Message, state: FSMContext) -> None:
#     data = await state.update_data(language=message.text)
#     await state.clear()
#     text = (
#         "Thank for all! Python is in my hearth!\nSee you soon."
#         if message.text.casefold() == "python"
#         else "Thank for information!\nSee you soon."
#     )
#     await message.answer(text)
#     await show_summary(message=message, data=data)
#
#
# async def show_summary(message: Message, data: Dict[str, Any], positive: bool = True) -> None:
#     name = data["name"]
#     language = data.get("language", "<something unexpected>")
#     text = f"I'll keep in mind that, {html.quote(name)}, "
#     text += (
#         f"you like to write bots with {html.quote(language)}."
#         if positive
#         else "you don't like to write bots, so sad..."
#     )
#     await message.answer(text=text, reply_markup=ReplyKeyboardRemove())
#
#
# @router.message(Command("cancel"))
# @router.message(F.text.casefold() == "cancel")
# async def cancel_handler(message: Message, state: FSMContext) -> None:
#     """
#     Allow user to cancel any action
#     """
#     current_state = await state.get_state()
#     if current_state is None:
#         return
#
#     logging.info("Cancelling state %r", current_state)
#     await state.clear()
#     await message.answer(
#         "Cancelled.",
#         reply_markup=ReplyKeyboardRemove(),
#     )

# print(f"-----TEST-----")
#
# import bcrypt
#
#
# password = 'swipe'
# print(password, 1)
# password = password.encode('utf-8')
# print(password, 2)
# hashed = bcrypt.hashpw(password, bcrypt.gensalt(10))
# print(hashed, 3)
# check = 'swipe1'
# print(check, 4)
# check = check.encode('utf-8')
# print(check, 5)
# print(bcrypt.checkpw(check, hashed))
