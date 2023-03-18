from core import *

from .assets import text, keyboard


class Controller(BaseController):

    async def callback(self):
        await self.state.finish()
        await self.answer(text, keyboard)
