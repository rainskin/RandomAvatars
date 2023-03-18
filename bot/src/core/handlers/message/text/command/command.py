from telegram import ext

from ..text import Text


class Command(Text):
    trigger: str | list[str]

    @classmethod
    def build(cls):
        cls.validate_fields('command')
        return ext.CommandHandler(cls.trigger, cls.handle, Text.filters)
