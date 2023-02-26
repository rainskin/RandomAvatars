from core import BaseApi
from lib.assets import enums


class PictureCategory(BaseApi):

    def get(self) -> str:
        return self._get()

    def set(self, category: enums.PictureCategory) -> bool:
        return self._set(
            params={'category': category},
        )
