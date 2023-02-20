from aiogram import types

from assets import PictureCategory, texts, kbs
from loader import db, api

Request = types.Message | types.CallbackQuery


class PictureRequest:
    _picture: list[str] = None

    def __init__(self, request: Request, category: PictureCategory):
        self._require_keyboard = False
        self._user_id = request.from_user.id
        self._category = category

        if isinstance(request, types.CallbackQuery):
            self._require_keyboard = True
            self._message = request.message
        else:
            self._message = request

        self._chat = self._message.chat
        db.save_chat(self._message.chat.id)

    async def respond(self):
        cooldown = await api.get_cooldown(self._user_id, self._chat.type)

        if cooldown:
            await self._ask_wait(cooldown)
        else:
            self._picture = await api.get_picture(self._category, self._chat.id)
            await self._try_answer()

    def _ask_wait(self, remaining_cooldown: int):
        text = texts.wait_for.format(time=remaining_cooldown)
        return self._message.answer(text, reply=True)

    async def _try_answer(self):
        await self._answer()

        await api.set_cooldown(self._user_id)

        if self._require_keyboard:
            kb = kbs.PictureMenu().create()
            await self._message.answer(texts.picture_menu_hint, reply_markup=kb)
            await api.set_picture_category(self._category, self._user_id)

    async def _answer(self):
        photo_ids = self._picture

        if len(photo_ids) > 1:
            media = [types.InputMediaPhoto(i) for i in photo_ids]
            await self._message.answer_media_group(media)
        else:
            await self._message.answer_photo(photo_ids[0])
