import config
from assets import commands
from core import *


async def update_my_commands():
    await bot.set_my_commands(commands.Groups.USER)

    for admin_id in config.ADMIN_IDS:
        with suppress(TelegramAPIError):
            scope = BotCommandScopeChat(admin_id)
            await bot.set_my_commands(commands.Groups.ADMIN, scope)
