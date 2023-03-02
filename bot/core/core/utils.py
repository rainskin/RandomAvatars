from .constants import *
from .dispatcher import dp, bot


async def get_invite_link(chat_id: int) -> str:
    chat = await bot.get_chat(chat_id)

    if not chat.invite_link:
        chat.invite_link = await chat.create_invite_link()

    return chat.invite_link


def reset_state():
    chat = CHAT.get_current()
    user = USER.get_current()
    return dp.storage.finish(chat=chat.id, user=user.id)
