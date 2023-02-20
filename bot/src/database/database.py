from core import BaseDatabase
from .models import Chat


class Database(BaseDatabase):

    @staticmethod
    def save_chat(chat_id: int):
        Chat.find_doc(id=chat_id) or Chat(id=chat_id).save()
