from core import TextHandler
from lib import PictureRequestHandler
from lib.Text import TRIGGERS_TO_CATEGORY


class Text(PictureRequestHandler, TextHandler):

    async def set_category(self):
        words = self.text.lower().split()

        for triggers, category in TRIGGERS_TO_CATEGORY:
            for word in words:
                if word in triggers:
                    self.category = category
                    return
