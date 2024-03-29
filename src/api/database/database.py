from collections import defaultdict

from assets.types import PictureCategory

from .models import Chat, Picture, User


class Database:  # TODO
    def __init__(self) -> None:
        self.pictures_by_category: dict[str, list[Picture]] = defaultdict(list)

    @staticmethod
    def get_chats() -> list[Chat]:
        return Chat.find_all()

    @staticmethod
    def save_chat(chat_id: int, utm: str | None) -> None:
        Chat.find(id=chat_id) or Chat(id=chat_id, utm=utm).save()

    @staticmethod
    def save_sent_picture(chat_id: int, picture: Picture) -> None:
        chat = Chat.get(chat_id)
        chat.save_sent_picture(picture)

    @staticmethod
    def get_user(user_id: int) -> User:
        return User.get(user_id)

    def get_pictures(self, category: PictureCategory, chat_id: int) -> list[Picture]:
        if not self.pictures_by_category:
            self._load_pictures()
        return self._get_new_pictures(category, chat_id)

    def _load_pictures(self):
        for p in Picture.find_all():
            self.pictures_by_category[p.category].append(p)

    def _get_new_pictures(self, category: PictureCategory, chat_id: int):
        chat = Chat.get(chat_id)
        pictures = self.pictures_by_category[category]
        new_pictures = [i for i in pictures if i.pk not in set(chat.sent_picture_ids)]

        if not new_pictures:
            new_pictures = pictures
            chat.reset_sent_pictures()

        return new_pictures


db = Database()
