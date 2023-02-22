from lib.core import bot
from lib.core import dp
from .consts import *


async def get_chat_invite_link(chat_id: int) -> str:
    chat = await bot.get_chat(chat_id)

    if not chat.invite_link:
        chat.invite_link = await chat.create_invite_link()

    return chat.invite_link


async def reset_state():
    chat = CHAT.get_current()
    user = USER.get_current()
    await dp.storage.finish(chat=chat.id, user=user.id)
