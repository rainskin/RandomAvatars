from .shortcuts import *
from .keyboards import Keyboard
from . import utils


class BaseController0:
    event: EVENT = None
    message: MESSAGE = None
    query: QUERY = None
    error: Exception = None

    def __init__(self, event_or_update: EVENT | UPDATE, error: Exception):
        self.error = error

        if isinstance(event_or_update, UPDATE):
            self.message = event_or_update.message
            self.query = event_or_update.callback_query
            self.event = self.message or self.query
            return

        self.event = event = event_or_update

        if isinstance(event, QUERY):
            self.query = event
        elif isinstance(event, MESSAGE):
            self.message = event

    def answer(self, text: str, keyboard: Keyboard = None):
        return utils.answer(self.event, text, keyboard)

    def answer_message(self, text: str, keyboard: Keyboard = None):
        return utils.answer_message(self.message, text, keyboard)

    def edit_message(self, text: str, keyboard: Keyboard = None):
        return utils.edit_message(self.query, text, keyboard)


class BaseController(BaseController0):

    async def callback(self):
        raise NotImplementedError()

    @classmethod
    def setup_on(cls, event):
        event(cls._handle)

    @classmethod
    async def _handle(cls, request: EVENT, error: Exception = None):
        handler = cls(request, error)
        result = await handler.callback()

        if handler.query:
            await handler.query.answer()

        return result
