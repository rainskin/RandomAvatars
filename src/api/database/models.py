from bson import ObjectId
from mongo import Document, PrimaryKey, me

from assets.types import PictureCategory


class Picture(Document):
    category: str
    photo_ids: list[str]


class Chat(Document):
    id: int | PrimaryKey  # noqa: A003
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
    id: int | PrimaryKey  # noqa: A003
    picture_category: str | None
    last_request_time: int = me.IntField(default=0)

    @classmethod
    def get(cls, user_id: int) -> "User":
        return super().get(user_id) or cls(id=user_id).save()

    def save_last_request_time(self, value: float):
        self.last_request_time = int(value)
        self.save()

    def save_picture_category(self, value: PictureCategory):
        self.picture_category = value
        self.save()


SettingValue = int | None


class Setting(Document):
    REQUIRED_JOIN_CHAT = "REQUIRED_JOIN_CHAT"

    id: str | PrimaryKey  # noqa: A003
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


class RequiredJoin(Document):
    chat_id: int = me.IntField(primary_key=True)
    link: str

    @classmethod
    def add(cls, chat_id: int, link: str):
        cls(chat_id=chat_id, link=link).save()

    @classmethod
    def remove(cls, chat_id: int):
        if doc := cls.get(chat_id):
            doc.delete()
