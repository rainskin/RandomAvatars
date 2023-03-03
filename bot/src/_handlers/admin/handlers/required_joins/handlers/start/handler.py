from core import BaseController

from .assets import keyboard
from .lib import get_text


class Controller(BaseController):

    async def callback(self):
        text = await get_text()
        await self.answer(text, keyboard)
