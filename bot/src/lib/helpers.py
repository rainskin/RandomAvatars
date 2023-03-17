from telegram import Chat, User

from .api import api


def save_chat(chat: Chat):
    return api.chats.save(chat.id)


def get_cooldown(user: User, chat: Chat):
    return api.user(user.id).cooldown.get(chat.type)


def get_picture(category: str, chat: Chat):
    return api.pictures(category).get_random(chat.id)


def set_cooldown(user: User):
    return api.user(user.id).cooldown.set()
