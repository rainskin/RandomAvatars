from core import TextHandler
from lib import PictureRequestHandler, get_picture_category, Menu


class GetAnother(PictureRequestHandler, TextHandler):
    trigger = Menu.Keyboard.GET_ANOTHER

    async def set_category(self):
        self.category = await get_picture_category(self.user)
