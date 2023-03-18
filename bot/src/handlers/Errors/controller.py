from core import *
from .assets import Texts, ErrorDescriptions


class Controller(BaseController):

    async def callback(self):
        error_desc = self.error.args[0]

        if error_desc == ErrorDescriptions.no_send_photo_rights:
            await self.ask_send_photo_rights()
            return True
        if error_desc == ErrorDescriptions.no_send_text_rights:
            return True

    async def ask_send_photo_rights(self):
        with suppress(BadRequest):
            await self.answer(Texts.no_send_photo_rights)
