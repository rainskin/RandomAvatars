from __future__ import annotations

from telegram import InlineKeyboardButton


class Url(InlineKeyboardButton):
    def __init__(self, text: str, url: str):
        super().__init__(text, url=url)

    def format(self, *args, **kwargs) -> Url:
        return Url(
            self.text.format(*args, **kwargs),
            self.url.format(*args, **kwargs),
        )
