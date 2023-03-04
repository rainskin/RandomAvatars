from core import BaseController

from ...lib import send_main_menu


class Controller(BaseController):

    async def callback(self):
        await send_main_menu(self.message)
