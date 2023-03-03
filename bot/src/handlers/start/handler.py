from aiogram.types import ChatType
from core import BaseHandler, utils

from lib import is_admin, update_my_commands, save_chat, send_main_menu
from .assets import group_text


class Handler(BaseHandler):

    async def callback(self):
        await utils.reset_state()
        await self._answer()

        if is_admin(self.message.from_user):
            await update_my_commands()

        await save_chat(self.message.chat)

    def _answer(self):
        if self.message.chat.type == ChatType.PRIVATE:
            return send_main_menu(self.message)
        return self.answer(group_text)
