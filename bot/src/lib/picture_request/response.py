from aiogram.types import InputMediaPhoto

from assets import PictureCategory, keyboards, texts
from core import *
from ..api import api


class Response:
    def __init__(
            self,
            picture: list[str],
            message: MESSAGE,
            user_id: int,
            category: PictureCategory,
            require_keyboard: bool,
    ):
        self._picture = picture
        self._message = message
        self._user_id = user_id
        self._category = category
        self._require_keyboard = require_keyboard

    async def send(self):
        await self._send_picture()
        await api.user(self._user_id).cooldown.set()

        if self._require_keyboard:
            await utils.answer(self._message, texts.picture_menu_hint, keyboards.picture_menu)
            await api.user(self._user_id).picture_category.set(self._category)

    async def _send_picture(self):
        photo_ids = self._picture

        if len(photo_ids) > 1:
            media = [InputMediaPhoto(i) for i in photo_ids]
            await self._message.answer_media_group(media)
        else:
            await self._message.answer_photo(photo_ids[0])
