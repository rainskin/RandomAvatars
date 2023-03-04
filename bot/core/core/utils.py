from .dispatcher import dp, bot
from .keyboards import BaseKeyboard
from .shortcuts import *


async def get_invite_link(chat_id: int) -> str:
    chat = await bot.get_chat(chat_id)

    if not chat.invite_link:
        chat.invite_link = await chat.create_invite_link()

    return chat.invite_link


def reset_state():
    chat = CHAT.get_current()
    user = USER.get_current()
    return dp.storage.finish(chat=chat.id, user=user.id)


def answer(event: EVENT, text: str, keyboard: BaseKeyboard = None):
    if isinstance(event, MESSAGE):
        return answer_message(event, text, keyboard)
    return edit_message(event, text, keyboard)


def answer_message(msg: MESSAGE, text: str, keyboard: BaseKeyboard = None):
    reply_markup = keyboard.create() if keyboard else None
    return msg.answer(text, reply_markup=reply_markup)


def edit_message(query: QUERY, text: str, keyboard: BaseKeyboard = None):
    reply_markup = keyboard.create() if keyboard else None
    return query.message.edit_text(text, reply_markup=reply_markup)
