from core import handlers
from lib.GetCommands import CATEGORY_BY_TRIGGER
from lib.handlers import PictureRequest


class GetCommands(PictureRequest, handlers.Command):
    trigger = list(CATEGORY_BY_TRIGGER)

    async def set_category(self):
        self.category = CATEGORY_BY_TRIGGER[self.command]
