from core import handlers
from lib.Text import TRIGGERS_TO_CATEGORY
from lib.handlers import PictureRequest


class Text(PictureRequest, handlers.Text):

    async def set_category(self):
        words = self.text.lower().split()

        for triggers, category in TRIGGERS_TO_CATEGORY:
            for word in words:
                if word in triggers:
                    self.category = category
                    return
