from telegram import Update, Message, Chat, User
from telegram.ext import ContextTypes, BaseHandler

from core import helpers


class Handler:

    def __init__(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        self.update = update
        self.context = context
        self.message: Message = update.effective_message
        self.chat: Chat = update.effective_chat
        self.user: User = update.effective_user
        self.query = update.callback_query

    @classmethod
    def build(cls) -> BaseHandler:
        raise NotImplementedError()

    @classmethod
    def validate_fields(cls, *names: str):  # TODO: remove
        helpers.validate_fields(cls, *names)
