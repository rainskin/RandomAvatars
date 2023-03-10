from collections import defaultdict

from core import BaseDatabase
from enums import PictureCategory
from .models import Picture, Chat, User, Setting


class Database(BaseDatabase):

    def __init__(self):
        self.pictures_by_category: dict[str, list[Picture]] = defaultdict(list)

    @staticmethod
    def get_chats() -> list[Chat]:
        return Chat().find_docs()

    @staticmethod
    def save_chat(chat_id: int):
        Chat.find_doc(id=chat_id) or Chat(id=chat_id).save()

    @staticmethod
    def save_sent_picture(chat_id: int, picture: Picture):
        chat = Chat.get(chat_id)
        chat.save_sent_picture(picture)

    @staticmethod
    def get_user(user_id: int) -> User:
        return User.get(user_id)

    def get_pictures(self, category: PictureCategory, chat_id: int) -> list[Picture]:
        if not self.pictures_by_category:
            self._load_pictures()
        return self._get_new_pictures(category, chat_id)

    def _load_pictures(self):
        for p in Picture.find_docs():
            self.pictures_by_category[p.category].append(p)

    def _get_new_pictures(self, category: PictureCategory, chat_id: int):
        chat = Chat.get(chat_id)
        pictures = self.pictures_by_category[category]
        new_pictures = [i for i in pictures if i.id not in set(chat.sent_picture_ids)]

        if not new_pictures:
            new_pictures = pictures
            chat.reset_sent_pictures()

        return new_pictures

    @staticmethod
    def set_required_join_chat(chat_id: int):
        setting = Setting.get(Setting.REQUIRED_JOIN_CHAT)
        setting.set_value(chat_id)

    @staticmethod
    def get_required_join_chat() -> int:
        setting = Setting.get(Setting.REQUIRED_JOIN_CHAT)
        return setting.value
