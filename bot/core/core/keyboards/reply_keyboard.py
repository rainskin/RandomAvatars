from aiogram.types import ReplyKeyboardMarkup

from .keyboard import BaseKeyboard


class ReplyKeyboard(BaseKeyboard[ReplyKeyboardMarkup]):
    def __new__(cls, *args, **kwargs):
        obj = super().__new__(cls)
        obj._raw = ReplyKeyboardMarkup(resize_keyboard=True)
        return obj

    def add_row(self, *buttons: str):
        self._raw.row(*buttons)

    def add_rows(self, *buttons: str, width: int = 1):
        button_rows = [buttons[i:i + width] for i in range(0, len(buttons), width)]
        for row in button_rows:
            self.add_row(*row)

    def create(self) -> ReplyKeyboardMarkup:
        return self._raw
