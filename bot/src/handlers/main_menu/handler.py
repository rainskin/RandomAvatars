from core import BaseHandler

from lib import on_text


class Handler(BaseHandler):

    async def callback(self):
        await on_text(self.event)
