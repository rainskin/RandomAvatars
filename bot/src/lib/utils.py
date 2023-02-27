import config
from core import bot, dp
from core.constants import *
from .assets import commands, PictureCategory
from .loader import api


async def get_chat_invite_link(chat_id: int) -> str:
    chat = await bot.get_chat(chat_id)

    if not chat.invite_link:
        chat.invite_link = await chat.create_invite_link()

    return chat.invite_link


async def reset_state():
    chat = CHAT.get_current()
    user = USER.get_current()
    await dp.storage.finish(chat=chat.id, user=user.id)


def save_chat(chat: CHAT):
    return api.chats.save(chat.id)


def reset_required_join():
    return api.required_join.set_chat_id(None)


def is_admin(user: USER) -> bool:
    return user.id in config.ADMIN_IDS


def contain_trigger_words(text: str, trigger_words: list[str]) -> bool:
    text_words = text.split()

    for tw in trigger_words:
        if tw in text_words:
            return True

    return False


def update_my_commands():
    return commands.setup()


async def get_picture_category(for_user: USER) -> PictureCategory | None:
    return await api.user(for_user.id).picture_category.get()
