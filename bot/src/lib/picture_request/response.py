from aiogram.types import InputMediaPhoto

from assets import PictureCategory
from core import *
from ..api import api


class Response:
    def __init__(
            self,
            picture: list[str],
            message: MESSAGE,
            user_id: int,
            category: PictureCategory,
    ):
        self._picture = picture
        self._message = message
        self._user_id = user_id
        self._category = category

    async def send(self) -> bool:
        await self._send_picture()
        await api.user(self._user_id).cooldown.set()
        return True

    async def _send_picture(self):
        photo_ids = self._picture

        if len(photo_ids) > 1:
            media = [InputMediaPhoto(i) for i in photo_ids]
            await self._message.answer_media_group(media)
        else:
            await self._message.answer_photo(photo_ids[0])
