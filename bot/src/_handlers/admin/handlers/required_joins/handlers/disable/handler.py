from core import BaseController

from lib import api
from .assets import text


class Controller(BaseController):

    async def callback(self):
        await api.required_join.reset()
        await self.answer(text)
