from core import *

from .assets import text, main_keyboard


class Controller(BaseController):

    async def callback(self):
        await self.answer(text, main_keyboard)
