from core import *
from lib import api
from .assets import Texts


class Controller(BaseController):

    async def callback(self):
        channel = self.message.forward_from_chat

        if not channel:
            return await self.answer(Texts.forward_error)

        try:
            await utils.get_invite_link(channel.id)
        except TelegramAPIError:
            return await self.answer(Texts.rights_error)

        await self.state.finish()
        await api.required_join.set_chat_id(channel.id)
        await self.answer(Texts.success)
