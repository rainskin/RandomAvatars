from collections import defaultdict

from assets import PictureCategory
from core import BaseDatabase
from .models import Picture, User, Chat


class Database(BaseDatabase):

    def __init__(self):
        self.pictures_by_category: dict[str, list[Picture]] = defaultdict(list)

    @staticmethod
    def get_user(user_id: int) -> User:
        return User.find_doc(id=user_id) or User(id=user_id).save()

    @staticmethod
    def save_chat(chat_id: int):
        Chat(id=chat_id).save()

    def get_pictures(self, category: PictureCategory) -> list[Picture]:
        if not self.pictures_by_category:
            self._load_pictures()

        return self.pictures_by_category[category]

    def _load_pictures(self):
        for p in Picture.find_docs():
            self.pictures_by_category[p.category].append(p)
