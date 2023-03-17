from core import BaseApi
from lib import assets


class PictureCategory(BaseApi):

    def get(self) -> str:
        return self._get()

    def set(self, category: assets.PictureCategory) -> bool:
        return self._set(
            params={'category': category},
        )
