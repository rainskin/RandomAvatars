from telegram import ext

from ..message import Message


class Text(Message):
    button: str | list[str] = None

    @classmethod
    def get_filters(cls):
        if cls.button:
            text_filter = ext.filters.Text(cls.button)
        else:
            text_filter = ext.filters.TEXT

        return cls.filters & text_filter
