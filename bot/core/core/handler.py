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

    def __init__(self, request: REQUEST):
        self.request = request

        if isinstance(request, QUERY):
            self.query = request
        else:
            self.message = request

    def answer_or_edit(self, text: str, keyboard: Keyboard = None):
        return answers.answer_or_edit(self.request, text, keyboard)

    answer = answer_or_edit

    @classmethod
    async def _handle(cls, request: REQUEST):
        handler = cls(request)
        await handler.callback()

        if handler.query:
            await handler.query.answer()

    @classmethod
    def setup(cls, event):
        event(cls._handle)
