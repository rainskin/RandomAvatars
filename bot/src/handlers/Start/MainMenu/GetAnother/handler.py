import lib
from core import handlers
from lib.handlers import PictureRequest
from lib.helpers import get_picture_category


class GetAnother(PictureRequest, handlers.Text):
    trigger = lib.MainMenu.Keyboard.GET_ANOTHER

    async def set_category(self):
        self.category = await get_picture_category(self.user)
