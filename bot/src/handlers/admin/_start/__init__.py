from core import BaseHandler
from .assets import text, keyboard, event


class Handler(BaseHandler):

    async def callback(self):
        await self.answer(text, keyboard)


Handler.setup(event)
