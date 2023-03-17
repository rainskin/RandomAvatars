from core import *

from .assets import text
from .lib import Broadcast
from ..assets import Storage


class Controller(BaseController):

    async def callback(self):
        await self.schedule_broadcast()
        await self.state.finish()
        await self.answer(text)

    async def schedule_broadcast(self):
        post_id = await Storage(self).get_post_id()
        Broadcast(self.query.message.chat, post_id).schedule()
