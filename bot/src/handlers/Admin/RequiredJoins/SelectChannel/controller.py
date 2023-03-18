from core import BaseController

from .assets import text, keyboard, post_from_channel_state


class Controller(BaseController):

    async def callback(self):
        await post_from_channel_state.set()
        await self.answer(text, keyboard)
