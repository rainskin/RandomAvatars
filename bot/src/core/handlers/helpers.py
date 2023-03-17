from telegram import ReplyKeyboardRemove

from core.keyboards import ReplyMarkup
from .types import AnyKeyboard


def get_reply_markup(keyboard: AnyKeyboard = None) -> ReplyMarkup | None:
    if keyboard is ...:
        return None
    if keyboard is None:
        return ReplyKeyboardRemove()
    if keyboard:
        return build_keyboard(keyboard)


def build_keyboard(keyboard: AnyKeyboard) -> ReplyMarkup:
    if isinstance(keyboard, type):
        keyboard = keyboard()
    return keyboard.build()
