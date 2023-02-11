import mongoengine as me

from assets import PictureCategory
from core import BaseDatabase, Document


class User(Document):
    id: int = me.IntField(primary_key=True)
    picture_category: str = me.StringField()


class Database(BaseDatabase):

    def get_picture_category(self, user_id: int) -> str:
        user = self.get_user(user_id)
        return user.picture_category

    def save_picture_category(self, user_id: int, picture_category: PictureCategory):
        user = self.get_user(user_id)
        user.picture_category = picture_category
        user.save()

    @staticmethod
    def get_user(user_id: int) -> User:
        return User.find_doc(id=user_id) or User(id=user_id).save()
