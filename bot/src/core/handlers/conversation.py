from typing import NewType

from telegram import ext
from core.helpers import listify
from .handler import Handler

State = NewType('State', int)  # TODO: generator


class Conversation(Handler):
    entry_point: Handler | list[Handler] = None
    subhandlers: dict[State, Handler] = None
    fallback: Handler | list[Handler] = None

    @classmethod
    def build(cls):
        cls.validate_fields('entry_point', 'subhandlers')
        entry_points = [h.build() for h in listify(cls.entry_point)]
        fallbacks = [h.build() for h in listify(cls.fallback or [])]
        states = {state: [handler.build()] for state, handler in cls.subhandlers.items()}
        return ext.ConversationHandler(
            entry_points,
            states,
            fallbacks,
            allow_reentry=True,
            name=cls.get_name(),
            persistent=True,
        )

    @classmethod
    def get_name(cls):
        return ':'.join([cls.__module__, cls.__name__])
