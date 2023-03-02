from contextlib import suppress

from aiogram.types import ChatType
from aiogram.utils.exceptions import BadRequest

from core.answers import answer
from core.constants import *
from lib.assets import texts, kbs
from . import requests, main_menu


def does_not_work(msg: MESSAGE):
    return answer(msg, texts.command_not_work)


def start(msg: MESSAGE):
    if msg.chat.type == ChatType.PRIVATE:
        return main_menu.send(msg)
    return answer(msg, texts.group_welcome)


async def no_send_photo_rights(update: UPDATE):
    if msg := update.message or update.callback_query.message:
        with suppress(BadRequest):
            await answer(msg, texts.no_send_photo_rights)


def ask_to_restart_bot(msg: MESSAGE):
    return answer(msg, texts.ask_restart, kbs.removed)
