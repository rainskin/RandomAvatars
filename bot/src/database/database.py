from core import BaseDatabase
from .models import User, Chat


class Database(BaseDatabase):

    @staticmethod
    def get_user(user_id: int) -> User:
        return User.find_doc(id=user_id) or User(id=user_id).save()

    @staticmethod
    def save_chat(chat_id: int):
        Chat(id=chat_id).save()

    @staticmethod
    def get_chats() -> list[Chat]:
        return Chat().find_docs()
