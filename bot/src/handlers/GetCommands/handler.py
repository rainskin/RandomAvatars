from core import CommandHandler
from lib import PictureRequestHandler
from lib.GetCommands import CATEGORY_BY_TRIGGER


class GetCommands(PictureRequestHandler, CommandHandler):
    trigger = list(CATEGORY_BY_TRIGGER)

    async def set_category(self):
        self.category = CATEGORY_BY_TRIGGER[self.command]
