from core import BaseDatabase


class Database(BaseDatabase):

    def get_picture_category(self, user_id: int):
        user = self.get_user(user_id)
        return user.picture_category

    @staticmethod
    def get_user(user_id: int):
        return User()


class User:
    picture_category = 'cute'
