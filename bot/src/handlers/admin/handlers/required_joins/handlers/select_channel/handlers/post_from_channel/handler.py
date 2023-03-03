from aiogram.utils.exceptions import TelegramAPIError
from core import utils, BaseHandler

from lib import api
from .assets import rights_error_text, forward_error_text, success_text


class Handler(BaseHandler):

    async def callback(self):
        channel = self.message.forward_from_chat

        if not channel:
            return await self.answer(forward_error_text)

        try:
            await utils.get_invite_link(channel.id)
        except TelegramAPIError:
            return await self.answer(rights_error_text)

        await utils.reset_state()
        await api.required_join.set_chat_id(channel.id)
        await self.answer(success_text)
