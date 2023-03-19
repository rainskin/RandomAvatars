from telegram import Update, ext

from .handler import Handler


class UpdateHandler(Handler):
    next_state: str | None = ...

    async def callback(self):
        raise NotImplementedError()

    async def prepare(self):
        pass

    async def post(self):
        pass

    @classmethod
    async def handle(cls, update: Update, context: ext.ContextTypes.DEFAULT_TYPE):
        handler = cls(update, context)
        await handler.prepare()
        await handler.callback()
        await handler.post()

        if handler.query:
            await handler.answer()

        next_state = handler.next_state

        if next_state is ...:
            next_state = None
        elif next_state is None:
            next_state = ext.ConversationHandler.END

        return next_state

    @classmethod
    def build(cls):
        return ext.TypeHandler(Update, cls.handle)
