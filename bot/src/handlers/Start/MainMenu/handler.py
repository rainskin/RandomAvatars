import lib
from lib import api, handlers
from lib.MainMenu import text, Keyboard


class MainMenu(handlers.PictureRequest):
    button = lib.Start.Keyboard.buttons

    def pick_category(self):
        button = self.query.data
        return lib.Start.CATEGORY_BY_BUTTON[button]

    async def post_reply(self):
        await self.reply(text, Keyboard)
        await api.user(self.user.id).picture_category.set(self.category)
