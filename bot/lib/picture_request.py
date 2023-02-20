import time

import config
from aiogram import types
from aiogram.types import ChatType
from aiogram.utils.exceptions import WrongFileIdentifier
from assets import PictureCategory, texts, kbs
from loader import db, logger, client

Request = types.Message | types.CallbackQuery


class PictureRequest:
    _picture: list[str] = None

    def __init__(self, request: Request, category: PictureCategory):
        self._require_keyboard = False
        self._user = db.get_user(request.from_user.id)
        self._category = category

        if isinstance(request, types.CallbackQuery):
            self._require_keyboard = True
            self._message = request.message
        else:
            self._message = request

        db.save_chat(self._message.chat)

    async def respond(self):
        cooldown = self._get_remaining_cooldown()

        if cooldown:
            await self._ask_wait(cooldown)
        else:
            self._picture = await _get_random_picture(self._category)
            await self._try_answer()

    def _ask_wait(self, remaining_cooldown: int):
        text = texts.wait_for.format(time=remaining_cooldown)
        return self._message.answer(text, reply=True)

    async def _try_answer(self):
        try:
            await self._answer()
        except WrongFileIdentifier:
            logger.error(f'WrongFileIdentifier: {self._picture}')
            return

        self._user.save_last_request_time(time.time())

        if self._require_keyboard:
            self._user.save_picture_category(self._category)
            kb = kbs.PictureMenu().create()
            await self._message.answer(texts.picture_menu_hint, reply_markup=kb)

    async def _answer(self):
        photo_ids = self._picture

        if len(photo_ids) > 1:
            media = [types.InputMediaPhoto(i) for i in photo_ids]
            await self._message.answer_media_group(media)
        else:
            await self._message.answer_photo(photo_ids[0])

    def _get_remaining_cooldown(self) -> int:
        if self._message.chat.type == ChatType.PRIVATE:
            return 0

        delta = int(time.time() - self._user.last_request_time)
        return max(0, config.REQUEST_COOLDOWN - delta)


async def _get_random_picture(category: PictureCategory) -> list[str]:
    base_url = f'http://{config.API_HOST}:8000'
    resp = await client.get(f'{base_url}/picture/{category}')
    return resp.json()
