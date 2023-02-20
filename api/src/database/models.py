import mongoengine as me

from core import Document


class Picture(Document):
    category: str = me.StringField()
    photo_ids: list[str] = me.ListField(me.StringField())
