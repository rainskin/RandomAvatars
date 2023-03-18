from telegram import ext

from core.helpers import validate_fields
from ...message import Message


class Command(Message):
    trigger: str | list[str] = None

    @classmethod
    def build(cls):
        validate_fields(cls, 'trigger')
        return ext.CommandHandler(cls.trigger, cls.handle, cls.get_filters())
