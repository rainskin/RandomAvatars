from __future__ import annotations

from abc import ABC, abstractmethod
from typing import TypeVar, Generic

from aiogram.types import InlineKeyboardButton, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, ReplyKeyboardRemove, ReplyKeyboardMarkup

RawKeyboardT = TypeVar('RawKeyboardT', ReplyKeyboardMarkup, InlineKeyboardMarkup, ReplyKeyboardRemove)
RawButtonT = TypeVar('RawButtonT', InlineKeyboardButton, KeyboardButton)


class BaseKeyboard(ABC, Generic[RawKeyboardT]):
    _raw: RawKeyboardT = None

    @abstractmethod
    def create(self) -> RawKeyboardT:
        pass


class Button(ABC, Generic[RawButtonT]):

    @abstractmethod
    def create(self) -> RawButtonT:
        pass

    @abstractmethod
    def format(self) -> Button:
        pass
