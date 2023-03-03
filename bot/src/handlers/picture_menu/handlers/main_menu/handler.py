from core import BaseHandler

from lib import send_main_menu


class Handler(BaseHandler):

    async def callback(self):
        await send_main_menu(self.message)
