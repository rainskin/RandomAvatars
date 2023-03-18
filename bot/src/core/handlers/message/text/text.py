from telegram import ext

from ..message import Message


class Text(Message):
    trigger: str | list[str] = None

    @classmethod
    def get_filters(cls):
        if cls.trigger:
            text_filter = ext.filters.Text(cls.trigger)
        else:
            text_filter = ext.filters.TEXT

        return cls.filters & text_filter
