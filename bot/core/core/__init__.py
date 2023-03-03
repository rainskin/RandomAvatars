from contextlib import suppress

from aiogram.types import BotCommand, BotCommandScopeChat
from aiogram.utils.deep_linking import get_start_link, get_startgroup_link
from aiogram.utils.exceptions import TelegramAPIError, BadRequest

from .api import BaseApi
from .app import app
from .bot import bot
from .dispatcher import dp
from .env import env
from .handler import BaseHandler
from .shortcuts import *

__all__ = [
    'env',
    'app',
    'dp',
    'bot',
    'BaseHandler',
    'BaseApi',
    'UPDATE',
    'MESSAGE',
    'QUERY',
    'USER',
    'CHAT',
    'EVENT',
    'CHAT_TYPES',
    'TelegramAPIError',
    'BadRequest',
    'BotCommand',
    'BotCommandScopeChat',
    'get_start_link',
    'get_startgroup_link',
    'suppress',
    'utils',
]
