from abc import ABC

from telegram import Update
from telegram.ext import ContextTypes

from . import layer2


class Handler(layer2.Handler, ABC):
    next_state: str = None

    async def callback(self):
        pass

    async def prepare(self):
        pass

    async def post(self):
        pass

    @classmethod
    async def handle(cls, update: Update, context: ContextTypes.DEFAULT_TYPE):
        handler = cls(update, context)
        await handler.prepare()
        await handler.callback()
        await handler.post()

        if handler.query:
            await handler.answer()

        return handler.next_state
