from aiogram import types
from aiogram.types import ChatType
from aiogram.utils.deep_linking import get_startgroup_link

import config
from assets import PictureCategory, texts, kbs, commands
from core import dp
from loader import api
from . import events, answers
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


def answer_start(msg: types.Message):
    if msg.chat.type == ChatType.PRIVATE:
        return answer_main_menu(msg)
    return msg.answer(texts.group_welcome)


def save_chat(chat: types.Chat):
    return api.save_chat(chat.id)


async def reset_state():
    chat = types.Chat.get_current()
    user = types.User.get_current()
    await dp.storage.finish(chat=chat.id, user=user.id)


def update_my_commands():
    return commands.setup()


def choose_picture_category(request: types.Message) -> PictureCategory | None:
    for word in get_words(request):
        for triggers, category in TRIGGERS_TO_CATEGORY:
            if word in triggers:
                return category


def get_words(msg: types.Message):
    return msg.text.split()

