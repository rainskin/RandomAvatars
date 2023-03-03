from . import answers
from .constants import *
from .keyboards import Keyboard


class BaseHandler:
    request: REQUEST = None
    message: MESSAGE = None
    query: QUERY = None
    text: str = None
    keyboard: Keyboard = None

    async def callback(self):
        raise NotImplementedError()

    def __init__(self, request: REQUEST | UPDATE, error: Exception):
        self.request = request
        self.error = error

        if isinstance(request, QUERY):
            self.query = request
        elif isinstance(request, MESSAGE):
            self.message = request
        else:
            self.message = request.message
            self.query = request.callback_query

    def answer_or_edit(self, text: str, keyboard: Keyboard = None):
        return answers.answer_or_edit(self.request, text, keyboard)

    answer = answer_or_edit

    @classmethod
    async def _handle(cls, request: REQUEST, error: Exception = None):
        handler = cls(request, error)
        result = await handler.callback()

        if handler.query:
            await handler.query.answer()

        return result

    @classmethod
    def setup(cls, event):
        event(cls._handle)
