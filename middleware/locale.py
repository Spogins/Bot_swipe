from typing import Any, Dict
from aiogram.types import TelegramObject
from aiogram.utils.i18n import I18nMiddleware
from configs.settings import REDIS


try:
    from babel import Locale, UnknownLocaleError
except ImportError:
    Locale = None

    class UnknownLocaleError(Exception):
        pass


class LocaleMiddleware(I18nMiddleware):

    async def get_locale(self, event: TelegramObject, data: Dict[str, Any]) -> str:
        event_from_user = data.get("event_from_user", None)
        redis_language = await REDIS.get(f'{event_from_user.id}')
        if redis_language is None:
            redis_language = await REDIS.set(f'{event_from_user.id}', self.i18n.default_locale)
            return redis_language

        if event_from_user is None or redis_language is None:
            return self.i18n.default_locale

        try:
            message_text = data.get('event_update').message.text
            if message_text.lower() == 'русский':
                await REDIS.set(f'{event_from_user.id}', 'ru')
                redis_language = await REDIS.get(f'{event_from_user.id}')
            if message_text.lower() == 'english':
                await REDIS.set(f'{event_from_user.id}', 'en')
                redis_language = await REDIS.get(f'{event_from_user.id}')
        except:
            if redis_language is not None:
                redis_language = redis_language.decode('utf-8')
            return redis_language

        if redis_language is not None:
            redis_language = redis_language.decode('utf-8')
        return redis_language