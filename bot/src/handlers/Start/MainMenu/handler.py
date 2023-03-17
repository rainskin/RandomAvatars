import lib
from lib import api, handlers
from lib.MainMenu import Texts, Keyboard


class MainMenu(handlers.PictureRequest):
    button = lib.Start.Keyboard.buttons

    def pick_category(self):
        button = self.query.data
        return lib.Start.CATEGORY_BY_BUTTON[button]

    async def on_success(self):
        await self.reply(Texts.menu_hint, Keyboard)
        await api.user(self.user.id).picture_category.set(self.category)
