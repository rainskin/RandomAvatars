from contextlib import suppress

from aiogram.utils.deep_linking import get_startgroup_link
from aiogram.utils.exceptions import BadRequest
from core.answers import answer
from core.constants import *

from lib.assets import texts
from assets import keyboards
from .requests import on_any_request, respond_picture


def does_not_work(msg: MESSAGE):
    return answer(msg, texts.command_not_work)


async def no_send_photo_rights(update: UPDATE):
    if msg := update.message or update.callback_query.message:
        with suppress(BadRequest):
            await answer(msg, texts.no_send_photo_rights)


def ask_to_restart_bot(msg: MESSAGE):
    return answer(msg, texts.ask_restart, keyboards.removed)


async def send_main_menu(msg: MESSAGE):
    text = texts.welcome.format(mention=msg.from_user.get_mention())
    startgroup_url = await get_startgroup_link('0')
    kb = keyboards.MainMenu(startgroup_url)
    await answer(msg, text, kb)
