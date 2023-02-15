import random
import time

from aiogram import types
from aiogram.types import ChatType
from aiogram.utils.exceptions import WrongFileIdentifier

import config
from assets import PictureCategory, texts, kbs
from database import models
from loader import db, logger

Request = types.Message | types.CallbackQuery


class PictureRequest:
    def __init__(self, request: Request, category: PictureCategory):
        self._require_keyboard = False
        self._user = db.get_user(request.from_user.id)
        self._category = category

        if isinstance(request, types.CallbackQuery):
            self._require_keyboard = True
            self._message = request.message
        else:
            self._message = request

        self._remaining_cooldown = self._get_remaining_cooldown()
        self._picture = _get_random_picture(category)
        db.save_chat(self._message.chat)

    def respond(self):
        if self._remaining_cooldown:
            return self._ask_wait()
        return self._try_answer()

    def _ask_wait(self):
        text = texts.wait_for.format(time=self._remaining_cooldown)
        return self._message.answer(text, reply=True)

    async def _try_answer(self):
        try:
            await self._answer()
        except WrongFileIdentifier:
            logger.error(f'WrongFileIdentifier: {self._picture.photo_ids}')
            return

        self._user.save_last_request_time(time.time())

        if self._require_keyboard:
            self._user.save_picture_category(self._category)
            kb = kbs.PictureMenu().create()
            await self._message.answer(texts.picture_menu_hint, reply_markup=kb)

    async def _answer(self):
        photo_ids = self._picture.photo_ids

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


def _get_request_message(request: Request) -> types.Message:
    if isinstance(request, types.CallbackQuery):
        return request.message
    return request


def _get_random_picture(category: PictureCategory) -> models.Picture:
    pictures = db.get_pictures(category)
    return random.choice(pictures)
