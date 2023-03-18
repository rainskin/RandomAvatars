from core import *

from .assets import text, confirm_state, keyboard, Storage


class Controller(BaseController):

    async def callback(self):
        await confirm_state.set()
        await Storage(self).set_post_id(self.message.message_id)
        await self.message.copy_to(self.message.chat.id)
        await self.answer(text, keyboard)
