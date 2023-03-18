from telegram import Chat, User

from .api import api
from .assets import PictureCategory


def save_chat(chat: Chat):
    return api.chats.save(chat.id)


def get_cooldown(user: User, chat: Chat):
    return api.user(user.id).cooldown.get(chat.type)


async def get_picture(category: str, chat: Chat) -> list[str]:
    return await api.pictures(category).get_random(chat.id)


def set_cooldown(user: User):
    return api.user(user.id).cooldown.set()


async def get_required_join() -> int:
    return await api.required_join.get_chat_id()


def save_picture_category(user: User, category: PictureCategory):
    return api.user(user.id).picture_category.set(category)


def get_picture_category(user: User):
    return api.user(user.id).picture_category.get()
