from core import BaseHandler

from .assets import text, keyboard


class Handler(BaseHandler):

    async def callback(self):
        await self.answer(text, keyboard)
