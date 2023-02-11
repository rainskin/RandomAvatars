from aiogram.types import ReplyKeyboardRemove

from .keyboard import Keyboard


class RemovedKeyboard(Keyboard[ReplyKeyboardRemove]):
    _raw = ReplyKeyboardRemove()

    def create(self) -> ReplyKeyboardRemove:
        return self._raw
