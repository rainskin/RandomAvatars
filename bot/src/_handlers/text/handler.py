from core import BaseController

from lib import on_text


class Controller(BaseController):

    async def callback(self):
        await on_text(self.event)
