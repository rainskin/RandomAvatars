from core import BaseController

from .assets import text, keyboard, post_state


class Controller(BaseController):

    async def callback(self):
        await post_state.set()
        await self.answer(text, keyboard)
