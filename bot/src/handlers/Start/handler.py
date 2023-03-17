import config
from core import handlers
from lib import commands
from lib.Start import Texts, Keyboard


# TODO: add save_chat, drop_state

class Start(handlers.Start):

    async def callback(self):
        if self.is_chat_private:
            text = Texts.for_private_chat.format(self.user_mention)
            keyboard = Keyboard(self.startgroup_url)
            await self.reply(text, keyboard)
        else:
            await self.reply(Texts.for_group)

        if self.is_user_admin:
            await self.update_commands()

    async def update_commands(self):
        await self.set_commands(commands.Groups.FOR_USERS)

        for admin_id in config.ADMIN_IDS:
            await self.set_commands(commands.Groups.FOR_ADMINS, admin_id)
