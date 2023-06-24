import asyncio
import logging
from aiogram.utils.i18n import I18n
from configs.settings import BOT, dp, LOCALES_DIR
from handlers.start import router as start_router
from handlers.registration import router as registration_router
from handlers.main_menu import router as menu_router
from handlers.advertisement import router as advertisement_router
from handlers.create_adv import router as create_adv_router
from handlers.profile import router as profile
from middleware.locale import LocaleMiddleware


async def main() -> None:

    i18n = I18n(path=LOCALES_DIR, default_locale="en", domain='messages')
    dp.message.outer_middleware(LocaleMiddleware(i18n))
    dp.callback_query.outer_middleware(LocaleMiddleware(i18n))

    dp.include_router(start_router)
    dp.include_router(registration_router)
    dp.include_router(menu_router)
    dp.include_router(advertisement_router)
    dp.include_router(create_adv_router)
    dp.include_router(profile)

    bot = BOT
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())