from telegram import ext

from . import mixins
from .helpers import get_reply_markup
from .types import AnyInlineKeyboard
from core.helpers import listify


class Query(mixins.Reply):
    button: str | list[str] = None
    edit_text: str = None
    edit_keyboard: AnyInlineKeyboard = ...

    @classmethod
    def build(cls):
        return ext.CallbackQueryHandler(cls.handle, cls._pattern)

    @classmethod
    def _pattern(cls, callback_data: str | object) -> bool:
        buttons = listify(cls.button)
        return callback_data in buttons

    async def callback(self):
        if self.edit_text:
            markup = get_reply_markup(self.edit_keyboard)
            await self.edit(self.edit_text, markup)
        if self.reply_text:
            await super().callback()
