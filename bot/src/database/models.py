import mongoengine as me
from bson import ObjectId

from core import Document


class Chat(Document):
    id: int = me.IntField(primary_key=True)
    sent_picture_ids: list[ObjectId] = me.ListField(me.ObjectIdField())
