from __future__ import annotations

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from .keyboard import Keyboard, Button


class InlineKeyboard(Keyboard[InlineKeyboardMarkup]):
    def __new__(cls, *args, **kwargs):
        obj = super().__new__(cls)
        obj._raw = InlineKeyboardMarkup()
        return obj

    def add_row(self, *buttons: CallbackButton | UrlButton | InlineQueryButton):
        raw_buttons = [button.create() for button in buttons]
        self._raw.row(*raw_buttons)

    def add_rows(self, *buttons: CallbackButton | UrlButton | InlineQueryButton, width: int = 1):
        button_rows = [buttons[i:i + width] for i in range(0, len(buttons), width)]
        for row in button_rows:
            self.add_row(*row)

    def create(self) -> InlineKeyboardMarkup:
        return self._raw


class CallbackButton(Button[InlineKeyboardButton]):
    def __init__(self, text: str, data: str = None):
        self._text = text
        self.data = data or text

    def format(self, **kwargs) -> CallbackButton:
        return CallbackButton(
            self._text.format(**kwargs),
            self.data.format(**kwargs),
        )

    def create(self) -> InlineKeyboardButton:
        return InlineKeyboardButton(self._text, callback_data=self.data)


class UrlButton(Button[InlineKeyboardButton]):
    def __init__(self, text: str, url: str):
        self._text = text
        self._url = url

    def format(self, **kwargs) -> UrlButton:
        return UrlButton(
            self._text.format(**kwargs),
            self._url.format(**kwargs),
        )

    def create(self) -> InlineKeyboardButton:
        return InlineKeyboardButton(self._text, url=self._url)


class InlineQueryButton(Button[InlineKeyboardButton]):
    def __init__(self, text: str, query: str = ''):
        self._text = text
        self._query = query

    def format(self, **kwargs) -> InlineQueryButton:
        return InlineQueryButton(
            self._text.format(**kwargs),
            self._query.format(**kwargs),
        )

    def create(self) -> InlineKeyboardButton:
        return InlineKeyboardButton(self._text, switch_inline_query_current_chat=self._query)
