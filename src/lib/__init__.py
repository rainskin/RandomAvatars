from contextlib import suppress

from aiogram.types import BotCommandScopeChat
from botty import TelegramAPIError, bot

from assets import ADMIN_COMMANDS, ADMIN_IDS, USER_COMMANDS

from .helpers import is_admin, pick_category, save_chat
from .picture_request import PictureRequest, on_picture_request

__all__ = (
    "is_admin",
    "save_chat",
    "pick_category",
    "on_picture_request",
    "PictureRequest",
)


async def set_commands():
    await bot.set_my_commands(USER_COMMANDS)
    for admin_id in ADMIN_IDS:
        with suppress(TelegramAPIError):
            scope = BotCommandScopeChat(admin_id)
            await bot.set_my_commands(ADMIN_COMMANDS, scope)
