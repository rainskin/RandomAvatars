from aiogram.types import ReplyKeyboardRemove

from .keyboard import BaseKeyboard


class RemovedKeyboard(BaseKeyboard[ReplyKeyboardRemove]):
    _raw = ReplyKeyboardRemove()

    def create(self) -> ReplyKeyboardRemove:
        return self._raw
