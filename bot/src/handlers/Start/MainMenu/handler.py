import lib
from lib import handlers
from lib.MainMenu import text, Keyboard
from lib.helpers import save_picture_category


class MainMenu(handlers.PictureRequest):
    button = lib.Start.Keyboard.buttons

    def set_category(self):
        button = self.query.data
        self.category = lib.Start.CATEGORY_BY_BUTTON[button]

    async def post_reply(self):
        await self.reply(text, Keyboard)
        await save_picture_category(self.user, self.category)
