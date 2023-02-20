import mongoengine as me

from assets import PictureCategory
from core import Document


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
