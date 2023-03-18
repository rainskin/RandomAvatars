import lib
from core import handlers
from lib.MainMenu import text, Keyboard, CATEGORY_BY_TRIGGER
from lib.handlers import PictureRequest
from lib.helpers import save_picture_category


class MainMenu(PictureRequest, handlers.Query):
    trigger = lib.Start.Keyboard.buttons

    def set_category(self):
        button = self.query.data
        self.category = CATEGORY_BY_TRIGGER[button]

    async def post_reply(self):
        await self.reply(text, Keyboard)
        await save_picture_category(self.user, self.category)
