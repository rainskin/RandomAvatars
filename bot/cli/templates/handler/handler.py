from core import BaseController

from .assets import text, keyboard, next_state


class Controller(BaseController):

    async def callback(self):
        await next_state.set()
        await self.answer(text, keyboard)
