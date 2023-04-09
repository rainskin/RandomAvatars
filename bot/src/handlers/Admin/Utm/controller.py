from core import *
from lib import get_utm
from .assets import text_item


class Controller(BaseController):

    async def callback(self):
        utm = await get_utm()
        strings = [
            text_item.format(key, count)
            for key, count in utm.items()
        ]
        text = '\n'.join(strings)
        await self.answer(text)
