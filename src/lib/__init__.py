import asyncio

from aiogram import types
from aiogram.utils.deep_linking import get_startgroup_link
from aiogram.utils.exceptions import TelegramAPIError, RetryAfter

import config
from assets import PictureCategory, texts, kbs
from loader import db
from .picture_request import PictureRequest, Request


def on_picture_request(request: Request, category: PictureCategory):
    return PictureRequest(request, category).respond()


def is_admin(user: types.User) -> bool:
    return user.id in config.ADMIN_IDS


async def answer_main_menu(msg: types.Message):
    text = texts.welcome.format(mention=msg.from_user.get_mention())
    startgroup_url = await get_startgroup_link('0')
    kb = kbs.MainMenu(startgroup_url).create()
    await msg.answer(text, reply_markup=kb)


async def ask_to_restart_bot(msg: types.Message):
    await msg.answer(texts.ask_restart, reply_markup=kbs.removed)


def contain_trigger_words(text: str, trigger_words: list[str]) -> bool:
    text_words = text.split()

    for tw in trigger_words:
        if tw in text_words:
            return True

    return False


TRIGGERS_TO_CATEGORY = [
    (config.TextTriggers.AVATAR, PictureCategory.AVATAR),
    (config.TextTriggers.PAIRED_AVATARS, PictureCategory.PAIRED_AVATARS),
    (config.TextTriggers.CUTE_PICTURE, PictureCategory.CUTE),
    (config.TextTriggers.ANGRY_PICTURE, PictureCategory.ANGRY),
]


def schedule_broadcast(post: types.Message):
    loop = asyncio.get_running_loop()
    loop.create_task(_broadcast(post))


async def _broadcast(post: types.Message):
    delivered_count = 0
    floods_count = 0
    errors_count = 0

    for chat in db.get_chats():
        try:
            await post.copy_to(chat.id)
        except RetryAfter as e:
            floods_count += 1
            await asyncio.sleep(e.timeout)
        except TelegramAPIError:
            errors_count += 1
        else:
            delivered_count += 1
        finally:
            await asyncio.sleep(0.1)

    text = texts.broadcast_summary.format(
        delivered_count=delivered_count,
        floods_count=floods_count,
        errors_count=errors_count,
    )
    await post.answer(text)
