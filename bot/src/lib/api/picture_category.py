from core import BaseApi
from lib.assets import enums


class PictureCategory(BaseApi):

    def get(self, user_id: int) -> str:
        return self._get(
            endpoint=f'/{user_id}',
        )

    def set(self, user_id: int, category: enums.PictureCategory) -> bool:
        return self._set(
            endpoint=f'/{user_id}',
            params={'category': category},
        )
