from core import BaseController
from lib import on_picture_request
from .lib import pick_category


class Controller(BaseController):

    async def callback(self):
        if category := pick_category(self.message):
            await on_picture_request(self.message, category)
