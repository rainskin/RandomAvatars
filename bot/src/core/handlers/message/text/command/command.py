from telegram import ext

from ..text import Text


class Command(Text):
    command: str

    @classmethod
    def build(cls):
        cls.validate_fields('command')
        return ext.CommandHandler(cls.command, cls.handle, Text.filters)
