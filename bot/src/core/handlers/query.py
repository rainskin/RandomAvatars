from telegram import ext

from core.helpers import listify
from . import mixins
from .helpers import get_reply_markup
from .types import AnyInlineKeyboard


class Query(mixins.Reply):
    trigger: str | list[str] = None
    edit_text: str = None
    edit_keyboard: AnyInlineKeyboard = ...

    @classmethod
    def build(cls):
        return ext.CallbackQueryHandler(cls.handle, cls._pattern)

    @classmethod
    def _pattern(cls, callback_data: str | object) -> bool:
        triggers = listify(cls.trigger)
        return callback_data in triggers

    async def callback(self):
        if self.edit_text:
            markup = get_reply_markup(self.edit_keyboard)
            await self.edit(self.edit_text, markup)
        if self.reply_text:
            await super().callback()
