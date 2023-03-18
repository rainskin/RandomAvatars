from core import StartHandler
from lib import commands, MenuRequestHandler, save_chat


class Start(StartHandler, MenuRequestHandler):
    async def post(self):
        if self.is_user_admin:
            await self.set_commands(commands.Groups.FOR_USERS, commands.Groups.FOR_ADMINS)
        await save_chat(self.chat)
