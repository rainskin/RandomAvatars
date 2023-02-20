from collections import defaultdict

from core import BaseDatabase
from enums import PictureCategory
from .models import Picture, Chat


class Database(BaseDatabase):

    def __init__(self):
        self.pictures_by_category: dict[str, list[Picture]] = defaultdict(list)

    @staticmethod
    def save_sent_picture(chat_id: int, picture: Picture):
        chat = Chat.get(chat_id)
        chat.save_sent_picture(picture)

    def get_pictures(self, category: PictureCategory, chat_id: int) -> list[Picture]:
        if not self.pictures_by_category:
            self._load_pictures()
        return self._get_new_pictures(category, chat_id)

    def _load_pictures(self):
        for p in Picture.find_docs():
            self.pictures_by_category[p.category].append(p)

    def _get_new_pictures(self, category: PictureCategory, chat_id: int):
        chat = Chat.get(chat_id)
        pictures = self.pictures_by_category[category]
        new_pictures = [i for i in pictures if i.id not in set(chat.sent_picture_ids)]

        if not new_pictures:
            last_sent_picture_id = chat.sent_picture_ids[-1]
            new_pictures = [i for i in pictures if i.id != last_sent_picture_id]
            chat.reset_sent_pictures()

        return new_pictures
