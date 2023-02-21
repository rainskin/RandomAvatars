from aiogram import types

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


async def ask_to_restart_bot(msg: types.Message):
    await msg.answer(texts.ask_restart, reply_markup=kbs.removed)


def contain_trigger_words(text: str, trigger_words: list[str]) -> bool:
    text_words = text.split()

    for tw in trigger_words:
        if tw in text_words:
            return True

    return False


TRIGGERS_TO_CATEGORY = [
    (config.TextTriggers.AVATAR + [commands.GET_AVATARS], PictureCategory.AVATAR),
    (config.TextTriggers.PAIRED_AVATARS + [commands.GET_PAIRED], PictureCategory.PAIRED_AVATARS),
    (config.TextTriggers.CUTE_PICTURE + [commands.GET_CUTE], PictureCategory.CUTE),
    (config.TextTriggers.ANGRY_PICTURE + [commands.GET_ANGRY], PictureCategory.ANGRY),
]


def schedule_broadcast(post: types.Message):
    Broadcast(post).schedule()


def save_chat(chat: types.Chat):
    return api.save_chat(chat.id)


async def reset_state():
    chat = types.Chat.get_current()
    user = types.User.get_current()
    await dp.storage.finish(chat=chat.id, user=user.id)


def update_my_commands():
    return commands.setup()


def choose_picture_category(request: types.Message | types.CallbackQuery) -> PictureCategory | None:
    if isinstance(request, types.Message):
        return _choose_picture_category_message(request)
    return _choose_picture_category_query(request)


def _choose_picture_category_message(request: types.Message) -> PictureCategory | None:
    if command := request.get_command(pure=True):
        words = [command]
    else:
        words = request.text.split()

    for word in words:
        for triggers, category in TRIGGERS_TO_CATEGORY:
            if word in triggers:
                return category


def _choose_picture_category_query(request: types.CallbackQuery) -> PictureCategory | None:
    kb = kbs.MainMenu

    match request.data:
        case kb.anime_avatars.data:
            return PictureCategory.AVATAR
        case kb.paired_avatars.data:
            return PictureCategory.PAIRED_AVATARS
        case kb.cute_pictures.data:
            return PictureCategory.CUTE
        case kb.angry_pictures.data:
            return PictureCategory.ANGRY


async def get_picture_category(for_user: types.User) -> PictureCategory | None:
    return await api.get_picture_category(for_user.id)
