from .constants import *
from .keyboards import Keyboard


def answer(msg: MESSAGE, text: str, keyboard: Keyboard = None):
    reply_markup = keyboard.create() if keyboard else None
    return msg.answer(text, reply_markup=reply_markup)


def edit(msg: MESSAGE, text: str, keyboard: Keyboard = None):
    reply_markup = keyboard.create() if keyboard else None
    return msg.edit_text(text, reply_markup=reply_markup)


def answer_or_edit(request: REQUEST, text: str, keyboard: Keyboard = None):
    if isinstance(request, MESSAGE):
        return answer(request, text, keyboard)
    return edit(request.message, text, keyboard)
