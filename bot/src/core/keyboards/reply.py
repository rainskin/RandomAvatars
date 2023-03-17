from telegram import ReplyKeyboardMarkup

from .keyboard import Keyboard
from .types import AnyReplyButton


class Reply(Keyboard):
    buttons: list[AnyReplyButton] = None

    def build(self) -> ReplyKeyboardMarkup:
        return ReplyKeyboardMarkup(self._prepared_buttons, resize_keyboard=True)
