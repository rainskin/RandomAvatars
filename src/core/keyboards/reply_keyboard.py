from aiogram.types import ReplyKeyboardMarkup

from .keyboard import Keyboard


class ReplyKeyboard(Keyboard[ReplyKeyboardMarkup]):
    def __new__(cls, *args, **kwargs):
        obj = super().__new__(cls)
        obj._raw = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        return obj

    def add_row(self, *buttons: str):
        self._raw.row(*buttons)

    def add_rows(self, *buttons: str):
        for button in buttons:
            self.add_row(button)

    def create(self) -> ReplyKeyboardMarkup:
        return self._raw
