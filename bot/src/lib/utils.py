from core import *
from .api import api


def save_chat(chat: CHAT, utm: str = None):
    return api.chats.save(chat.id, utm)


async def get_utm() -> dict:
    return await api.utm.get()
