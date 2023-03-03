from core import BaseHandler

from .assets import text


class Handler(BaseHandler):

    async def callback(self):
        await self.answer(text)
