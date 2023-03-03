from core import BaseHandler

from lib import on_any_request


class Handler(BaseHandler):

    async def callback(self):
        await on_any_request(self.request)
