from contextlib import suppress

from aiogram.types import BotCommand, BotCommandScopeChat
from aiogram.utils.exceptions import TelegramAPIError
from core import bot

import config

START = 'start'
GET_AVATARS = 'get_avatars'
GET_PAIRED = 'get_paired'
GET_CUTE = 'get_cute'
GET_ANGRY = 'get_angry'
SEND_PICTURE = 'send_picture'
ADMIN = 'admin'

_USER_COMMANDS = [
    BotCommand(START, 'Главное меню'),
    BotCommand(GET_AVATARS, 'Получить аватарку'),
    BotCommand(GET_PAIRED, 'Получить парные аватарки'),
    BotCommand(GET_CUTE, 'Получить милую пикчу'),
    BotCommand(GET_ANGRY, 'Получить агрессивную пикчу'),
    BotCommand(SEND_PICTURE, 'Отправить пикчу пользователю'),
]

_ADMIN_COMMANDS = _USER_COMMANDS + [
    BotCommand(ADMIN, 'Админ-панель'),
]


async def setup():
    await bot.set_my_commands(_USER_COMMANDS)

    for admin_id in config.ADMIN_IDS:
        with suppress(TelegramAPIError):
            await bot.set_my_commands(_ADMIN_COMMANDS, BotCommandScopeChat(admin_id))
