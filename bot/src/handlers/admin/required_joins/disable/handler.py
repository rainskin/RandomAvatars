from core import BaseHandler

from lib import api
from .assets import text


class Handler(BaseHandler):

    async def callback(self):
        await api.required_join.reset()
        await self.answer(text)
