from core import BaseController

from .lib import pick_category, on_picture_request


class Controller(BaseController):

    async def callback(self):
        if category := pick_category(self.message):
            await on_picture_request(self.message, category)
