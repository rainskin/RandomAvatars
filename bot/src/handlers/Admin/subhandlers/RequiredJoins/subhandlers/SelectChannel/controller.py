from core import BaseController

from .assets import text, keyboard, state


class Controller(BaseController):

    async def callback(self):
        await state.set()
        await self.answer(text, keyboard)
