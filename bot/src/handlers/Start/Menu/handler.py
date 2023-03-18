from core import QueryHandler
from lib import MenuKeyboard, save_picture_category, PictureRequestHandler
from lib.Menu import text, Keyboard, CATEGORY_BY_TRIGGER


class Menu(PictureRequestHandler, QueryHandler):
    trigger = MenuKeyboard.buttons

    async def set_category(self):
        button = self.query.data
        self.category = CATEGORY_BY_TRIGGER[button]

    async def post_reply(self):
        await self.reply(text, Keyboard)
        await save_picture_category(self.user, self.category)
