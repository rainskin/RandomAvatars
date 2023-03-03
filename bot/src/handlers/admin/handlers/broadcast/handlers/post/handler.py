from core import BaseHandler, utils

from .assets import text
from .lib import Broadcast


class Handler(BaseHandler):

    async def callback(self):
        await utils.reset_state()
        await self.answer(text)
        self.schedule_broadcast()

    def schedule_broadcast(self):
        Broadcast(self.message).schedule()
