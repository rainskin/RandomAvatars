from core import BaseHandler
from .assets import event, state, text, keyboard


class Handler(BaseHandler):

    async def callback(self):
        await state.set()
        await self.answer(text, keyboard)


Handler.setup(event)
