from contextlib import suppress

from aiogram.utils.exceptions import BadRequest
from core import BaseController

from .assets import no_send_photo_rights_text


class Controller(BaseController):

    async def callback(self):

        error_desc = self.error.args[0]

        if error_desc == 'Not enough rights to send photos to the chat':
            await self.no_send_photo_rights()
            return True
        if error_desc == 'Not enough rights to send text messages to the chat':
            return True

    async def no_send_photo_rights(self):
        with suppress(BadRequest):
            await self.message.answer(no_send_photo_rights_text)
