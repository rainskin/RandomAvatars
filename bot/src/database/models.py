import mongoengine as me
from bson import ObjectId

from assets import PictureCategory
from core import Document


class User(Document):
    id: int = me.IntField(primary_key=True)
    picture_category: str = me.StringField()
    last_request_time: int = me.IntField(default=0)

    def save_picture_category(self, picture_category: PictureCategory):
        self.picture_category = picture_category
        self.save()


class Chat(Document):
    id: int = me.IntField(primary_key=True)
    sent_picture_ids: list[ObjectId] = me.ListField(me.ObjectIdField())
