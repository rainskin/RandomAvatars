from core import *

from .assets import text, keyboard


class Controller(BaseController):

    async def callback(self):
        await utils.reset_state()
        await self.answer(text, keyboard)
