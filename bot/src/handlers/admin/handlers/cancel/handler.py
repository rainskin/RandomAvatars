from core import BaseHandler, utils

from .assets import text, keyboard


class Handler(BaseHandler):

    async def callback(self):
        await utils.reset_state()
        await self.answer(text, keyboard)
