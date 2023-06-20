import asyncio
import logging
from aiogram import Bot, Dispatcher
from aioredis import Redis
from aiogram.fsm.storage.redis import RedisStorage
from configs.settings import TOKEN, BOT
from handlers.start import router as start_router
from handlers.registration import router as registration_router
from handlers.main_menu import router as menu_router
from handlers.advertisement import router as advertisement_router
from handlers.create_adv import router as create_adv_router


async def main() -> None:
    # redis storage
    redis = Redis()
    storage = RedisStorage(redis=redis)
    # Dispatcher is a root router
    dp = Dispatcher(storage=storage)

    # ... and all other routers should be attached to Dispatcher
    dp.include_router(start_router)
    dp.include_router(registration_router)
    dp.include_router(menu_router)
    dp.include_router(advertisement_router)
    dp.include_router(create_adv_router)
    # Initialize Bot instance with a default parse mode which will be passed to all API calls
    bot = BOT
    # And the run events dispatching
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())