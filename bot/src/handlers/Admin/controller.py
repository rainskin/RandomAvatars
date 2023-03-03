from core import BaseController

from .assets import menu_text, main_keyboard


class Controller(BaseController):

    async def callback(self):
        await self.answer(menu_text, main_keyboard)
