from core import BaseController

from .assets import text


class Controller(BaseController):

    async def callback(self):
        await self.answer(text)
