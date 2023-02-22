from contextlib import suppress

from aiogram.types import ChatType
from aiogram.utils.deep_linking import get_startgroup_link
from aiogram.utils.exceptions import BadRequest, TelegramAPIError

from .assets import texts, kbs
from .loader import api
from .consts import *
from .utils import get_chat_invite_link, reset_state


def does_not_work(msg: MESSAGE):
    return msg.answer(texts.command_not_work)


def start(msg: MESSAGE):
    if msg.chat.type == ChatType.PRIVATE:
        return main_menu(msg)
    return msg.answer(texts.group_welcome)


async def main_menu(msg: MESSAGE):
    text = texts.welcome.format(mention=msg.from_user.get_mention())
    startgroup_url = await get_startgroup_link('0')
    kb = kbs.MainMenu(startgroup_url).create()
    await msg.answer(text, reply_markup=kb)


async def no_send_photo_rights(update: UPDATE):
    if msg := update.message or update.callback_query.message:
        with suppress(BadRequest):
            await msg.answer(texts.no_send_photo_rights)


def admin_panel(request: REQUEST):
    text = texts.admin_panel
    kb = kbs.admin_panel

    if isinstance(request, MESSAGE):
        return request.answer(text, reply_markup=kb)
    return request.message.edit_text(text, reply_markup=kb)


def ask_broadcast_post(query: QUERY):
    return query.message.edit_text(texts.ask_broadcast_post, reply_markup=kbs.admin_cancel)


def broadcast_started(msg: MESSAGE):
    return msg.answer('Начинаю рассылку..')


async def ask_to_restart_bot(msg: MESSAGE):
    await msg.answer(texts.ask_restart, reply_markup=kbs.removed)


async def on_post_from_channel(msg: MESSAGE):
    from_channel = msg.forward_from_chat

    if not from_channel:
        await msg.answer('Ошибка, не вижу источник пересылки')
        return

    try:
        await get_chat_invite_link(from_channel.id)
    except TelegramAPIError:
        await msg.answer('У меня нет нужных прав в этом канале')
        return

    await reset_state()
    await api.required_join.set_chat_id(from_channel.id)
    await msg.answer('Обязательная подписка настроена')


def ask_post_from_channel(query: QUERY):
    return query.message.edit_text(texts.ask_post_from_channel, reply_markup=kbs.admin_cancel)


def required_join_disabled(query: QUERY):
    return query.message.edit_text('Обязательная подписка отключена')


async def required_join_info(query: QUERY):
    required_chat_id = await api.required_join.get_chat_id()

    if required_chat_id:
        invite_link = await get_chat_invite_link(required_chat_id)
        text = f'Обязательная подписка: {invite_link}'
    else:
        text = f'Обязательная подписка отключена'

    await query.message.edit_text(text, reply_markup=kbs.required_join)
