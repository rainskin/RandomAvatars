import random
from contextlib import suppress

from aiogram.types import BotCommandScopeChat
from botty import bot, TelegramAPIError, User, Message

import api
from api import ADMIN_IDS, Sign
from assets import commands


async def set_commands():
    await bot.set_my_commands(commands.Groups.FOR_USERS)
    for admin_id in ADMIN_IDS:
        with suppress(TelegramAPIError):
            scope = BotCommandScopeChat(admin_id)
            await bot.set_my_commands(commands.Groups.FOR_ADMINS, scope)


def is_admin(user: User):
    return user.id in ADMIN_IDS


def save_chat(msg: Message):
    utm = msg.get_args() or None
    return api.save_chat(msg.chat.id, utm)


def get_random_sign() -> str | None:
    signs = [s.text for s in Sign.find_all()]
    return random.choice(signs) if signs else None
