from core import *
from .api import api


def save_chat(chat: CHAT):
    return api.chats.save(chat.id)
