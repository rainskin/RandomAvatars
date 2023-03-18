from core import handlers
from lib import commands
from lib.handlers import MenuRequest
from lib.helpers import save_chat


class Start(handlers.Start, MenuRequest):
    async def post(self):
        if self.is_user_admin:
            await self.set_commands(commands.Groups.FOR_USERS, commands.Groups.FOR_ADMINS)
        await save_chat(self.chat)
