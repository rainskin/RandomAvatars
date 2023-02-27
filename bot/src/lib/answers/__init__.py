from contextlib import suppress

from aiogram.types import ChatType
from aiogram.utils.deep_linking import get_startgroup_link
from aiogram.utils.exceptions import BadRequest, TelegramAPIError

from core.answers import answer, answer_or_edit
from core.constants import *
from lib.assets import texts, kbs
from lib.loader import api
from lib.utils import get_chat_invite_link, reset_state
from . import required_join, requests


def does_not_work(msg: MESSAGE):
    return answer(msg, texts.command_not_work)


def start(msg: MESSAGE):
    if msg.chat.type == ChatType.PRIVATE:
        return main_menu(msg)
    return answer(msg, texts.group_welcome)


async def main_menu(msg: MESSAGE):
    text = texts.welcome.format(mention=msg.from_user.get_mention())
    startgroup_url = await get_startgroup_link('0')
    kb = kbs.MainMenu(startgroup_url)
    await answer(msg, text, kb)


async def no_send_photo_rights(update: UPDATE):
    if msg := update.message or update.callback_query.message:
        with suppress(BadRequest):
            await answer(msg, texts.no_send_photo_rights)


def admin_panel(request: REQUEST):
    return answer_or_edit(request, texts.admin_panel, kbs.admin_panel)


def ask_broadcast_post(query: QUERY):
    return answer_or_edit(query, texts.ask_broadcast_post, kbs.admin_cancel)


def broadcast_started(msg: MESSAGE):
    return answer(msg, 'Начинаю рассылку..')


def ask_to_restart_bot(msg: MESSAGE):
    return answer(msg, texts.ask_restart, kbs.removed)


async def on_post_from_channel(msg: MESSAGE):
    from_channel = msg.forward_from_chat

    if not from_channel:
        await answer(msg, 'Ошибка, не вижу источник пересылки')
        return

    try:
        await get_chat_invite_link(from_channel.id)
    except TelegramAPIError:
        await answer(msg, 'У меня нет нужных прав в этом канале')
        return

    await reset_state()
    await api.required_join.set_chat_id(from_channel.id)
    await answer(msg, 'Обязательная подписка настроена')


def ask_post_from_channel(query: QUERY):
    return answer_or_edit(query, texts.ask_post_from_channel, kbs.admin_cancel)
