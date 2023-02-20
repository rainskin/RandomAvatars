from collections import defaultdict

from core import BaseDatabase
from enums import PictureCategory
from .models import Picture


class Database(BaseDatabase):

    def __init__(self):
        self.pictures_by_category: dict[str, list[Picture]] = defaultdict(list)

    def get_pictures(self, category: PictureCategory) -> list[Picture]:
        if not self.pictures_by_category:
            self._load_pictures()

        return self.pictures_by_category[category]

    def _load_pictures(self):
        for p in Picture.find_docs():
            self.pictures_by_category[p.category].append(p)
