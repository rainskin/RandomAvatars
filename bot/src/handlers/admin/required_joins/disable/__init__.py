from core import BaseHandler
from lib import api
from .assets import event, text


class Handler(BaseHandler):

    async def callback(self):
        await api.required_join.reset()
        await self.answer(text)


Handler.setup(event)
