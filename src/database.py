from collections import defaultdict

import mongoengine as me

from assets import PictureCategory
from core import BaseDatabase, Document


class User(Document):
    id: int = me.IntField(primary_key=True)
    picture_category: str = me.StringField()
    last_request_time: int = me.IntField(default=0)

    def save_picture_category(self, picture_category: PictureCategory):
        self.picture_category = picture_category
        self.save()

    def save_last_request_time(self, request_time: int):
        self.last_request_time = request_time
        self.save()


class Chat(Document):
    id: int = me.IntField(primary_key=True)


class Picture(Document):
    category: str = me.StringField()
    photo_ids: list[str] = me.ListField(me.StringField())


class Database(BaseDatabase):

    def __init__(self):
        self.pictures_by_category: dict[str, list[Picture]] = defaultdict(list)

    def get_pictures(self, category: PictureCategory) -> list[Picture]:
        if not self.pictures_by_category:
            self.load_pictures()

        return self.pictures_by_category[category]

    def load_pictures(self):
        for p in Picture.find_docs():
            self.pictures_by_category[p.category].append(p)

    @staticmethod
    def get_user(user_id: int) -> User:
        return User.find_doc(id=user_id) or User(id=user_id).save()

    @staticmethod
    def save_chat(chat_id: int):
        Chat(id=chat_id).save()
