from abc import ABC

from telegram import Update
from telegram.ext import ContextTypes

from core.helpers import validate_fields
from ..handler import Handler
from ..types import ReplyKeyboard


class Reply(Handler, ABC):
    reply_text: str = None
    reply_keyboard: ReplyKeyboard = ...
    reply_text2: str = None
    reply_keyboard2: ReplyKeyboard = ...
    next_state: str = None

    @classmethod
    async def handle(cls, update: Update, context: ContextTypes.DEFAULT_TYPE):
        handler = cls(update, context)
        await handler.prepare()
        await handler.callback()
        return handler.next_state

    async def prepare(self):
        pass

    async def callback(self):
        validate_fields(self, 'reply_text')
        await self._reply()
        if self.reply_text2:
            await self._reply(second=True)

    async def _reply(self, second=False):
        text = self.reply_text2 if second else self.reply_text
        keyboard = self.get_reply_keyboard2() if second else self.get_reply_keyboard()
        await self.reply(text, keyboard)

    def get_reply_keyboard(self) -> ReplyKeyboard:
        return self.reply_keyboard

    def get_reply_keyboard2(self) -> ReplyKeyboard:
        return self.reply_keyboard2
