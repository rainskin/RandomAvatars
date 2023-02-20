from __future__ import annotations

import mongoengine as me
from bson import ObjectId

from core import Document


class Picture(Document):
    category: str = me.StringField()
    photo_ids: list[str] = me.ListField(me.StringField())


class Chat(Document):
    id: int = me.IntField(primary_key=True)
    sent_picture_ids: list[ObjectId] = me.ListField(me.ObjectIdField())

    def reset_sent_pictures(self):
        self.sent_picture_ids = []
        self.save()

    @classmethod
    def get(cls, chat_id: int) -> Chat:
        return Chat.find_doc(id=chat_id) or Chat(id=chat_id).save()

    def save_sent_picture(self, picture: Picture):
        self.sent_picture_ids.append(picture.id)
        self.save()