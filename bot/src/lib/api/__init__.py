from lib.assets import PictureCategory
from core import BaseApi
from .required_join import RequiredJoin


class Api(BaseApi):

    def __init__(self, base_url: str):
        super().__init__(base_url)
        self.required_join = RequiredJoin(self._base_url + '/required-join')

    def get_picture(self, chat_id: int, category: PictureCategory) -> list[str]:
        return self._get(
            endpoint=f'/picture/{category}',
            params={'chat_id': chat_id},
        )

    def get_cooldown(self, user_id: int, chat_type: str) -> int:
        return self._get(
            endpoint=f'/cooldown/{user_id}',
            params={'chat_type': chat_type},
        )

    def set_cooldown(self, user_id: int) -> bool:
        return self._set(
            endpoint=f'/cooldown/{user_id}',
        )

    def get_picture_category(self, user_id: int) -> str:
        return self._get(
            endpoint=f'/picture-category/{user_id}',
        )

    def set_picture_category(self, user_id: int, category: PictureCategory) -> bool:
        return self._set(
            endpoint=f'/picture-category/{user_id}',
            params={'category': category},
        )

    def get_chats(self) -> list[int]:
        return self._get(
            endpoint=f'/chats',
        )

    def save_chat(self, chat_id: int) -> bool:
        return self._set(
            endpoint=f'/chats/{chat_id}',
        )
