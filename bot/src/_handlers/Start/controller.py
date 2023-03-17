import config
from core import *
from lib import save_chat
from .assets import group_welcome_text
from .lib import update_my_commands, send_main_menu


class Controller(BaseController):

    async def callback(self):
        await self.state.finish()
        await self._answer()

        if self.is_user_admin():
            await update_my_commands()

        await save_chat(self.message.chat)

    def _answer(self):
        if self.message.chat.type == CHAT_TYPES.PRIVATE:
            return send_main_menu(self.message)
        return self.answer(group_welcome_text)

    def is_user_admin(self):
        return self.message.from_user.id in config.ADMIN_IDS
