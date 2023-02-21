from contextlib import suppress

from aiogram import types
from aiogram.types import ChatType
from aiogram.utils.deep_linking import get_startgroup_link
from aiogram.utils.exceptions import BadRequest

from assets import texts, kbs


def does_not_work(msg: types.Message):
    return msg.answer(texts.command_not_work)


def start(msg: types.Message):
    if msg.chat.type == ChatType.PRIVATE:
        return main_menu(msg)
    return msg.answer(texts.group_welcome)


async def main_menu(msg: types.Message):
    text = texts.welcome.format(mention=msg.from_user.get_mention())
    startgroup_url = await get_startgroup_link('0')
    kb = kbs.MainMenu(startgroup_url).create()
    await msg.answer(text, reply_markup=kb)


def no_send_photo_rights(update: types.Update):
    if msg := update.message or update.callback_query.message:
        with suppress(BadRequest):
            return msg.answer(texts.no_send_photo_rights)
