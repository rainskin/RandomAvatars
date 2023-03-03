from core import BaseController

from .assets import text, keyboard


class Controller(BaseController):

    async def callback(self):
        await self.answer(text, keyboard)
