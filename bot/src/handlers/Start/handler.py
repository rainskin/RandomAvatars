from core import handlers
from lib import commands
from lib.Start import Texts, Keyboard
from lib.helpers import save_chat


class Start(handlers.Start):

    async def prepare(self):
        if self.is_chat_private:
            self.reply_text = Texts.for_private_chat.format(self.user_mention)
            self.reply_keyboard = Keyboard(self.startgroup_url)
        else:
            self.reply_text = Texts.for_group

    async def post(self):
        if self.is_user_admin:
            await self.set_commands(commands.Groups.FOR_USERS, commands.Groups.FOR_ADMINS)
        await save_chat(self.chat)
