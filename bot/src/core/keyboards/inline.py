from telegram import InlineKeyboardButton, InlineKeyboardMarkup

from .keyboard import Keyboard
from .types import AnyInlineButton


class Inline(Keyboard):
    buttons: list[AnyInlineButton] = None

    def build(self) -> InlineKeyboardMarkup:
        return InlineKeyboardMarkup(self._prepared_buttons)

    @staticmethod
    def _build_button(button: AnyInlineButton) -> InlineKeyboardButton:
        if isinstance(button, str):
            return InlineKeyboardButton(button, callback_data=button)
        return button
