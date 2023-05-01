from bson import ObjectId
from mongo import Document, PrimaryKey, me

from api.enums import PictureCategory


class Picture(Document):
    category: str
    photo_ids: list[str]


class Chat(Document):
    id: int | PrimaryKey
    utm: str | None
    sent_picture_ids: list[ObjectId]

    def reset_sent_pictures(self):
        self.sent_picture_ids = []
        self.save()

    @classmethod
    def get(cls, chat_id: int) -> "Chat":
        return super().get(chat_id) or cls(id=chat_id).save()

    def save_sent_picture(self, picture: Picture):
        self.sent_picture_ids.append(picture.pk)
        self.save()


class User(Document):
    id: int | PrimaryKey
    picture_category: str | None
    last_request_time: int = me.IntField(default=0)

    @classmethod
    def get(cls, user_id: int) -> "User":
        return super().get(user_id) or cls(id=user_id).save()

    def save_last_request_time(self, value: int):
        self.last_request_time = value
        self.save()

    def save_picture_category(self, value: PictureCategory):
        self.picture_category = value
        self.save()


SettingValue = int | None


class Setting(Document):
    REQUIRED_JOIN_CHAT = "REQUIRED_JOIN_CHAT"

    id: str | PrimaryKey
    value: SettingValue = me.DynamicField()

    @classmethod
    def get(cls, _id: int):
        return super().get(_id) or cls(id=_id).save()

    def set_value(self, value: SettingValue):
        self.value = value
        self.save()


class Sign(Document):
    text: str

    @classmethod
    def add(cls, text: str):
        cls(text=text).save()

    @classmethod
    def remove(cls, _id: str):
        if doc := cls.get(_id):
            doc.delete()
