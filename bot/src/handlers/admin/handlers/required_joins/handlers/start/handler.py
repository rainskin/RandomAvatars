from core import BaseHandler

from .assets import keyboard
from .lib import get_text


class Handler(BaseHandler):

    async def callback(self):
        text = await get_text()
        await self.answer(text, keyboard)
