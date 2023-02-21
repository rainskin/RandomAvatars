from aiogram import types
from aiogram.utils.deep_linking import get_startgroup_link

import config
from assets import PictureCategory, texts, kbs
from .broadcast import Broadcast
from .invite_links import get_chat_invite_link
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
    Broadcast(post).schedule()
