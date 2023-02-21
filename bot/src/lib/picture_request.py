from aiogram import types

from assets import PictureCategory, texts, kbs
from loader import api

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

    async def respond(self):
        cooldown = await api.get_cooldown(self._user_id, self._chat.type)

        if cooldown:
            await self._ask_wait(cooldown)
        else:
            self._picture = await api.get_picture(self._chat.id, self._category)
            await self._answer()

        await api.save_chat(self._chat.id)

    def _ask_wait(self, cooldown: int):
        text = texts.wait_for.format(time=cooldown)
        return self._message.answer(text, reply=True)

    async def _answer(self):
        await self._send_picture()
        await api.set_cooldown(self._user_id)

        if self._require_keyboard:
            await self._message.answer(texts.picture_menu_hint, reply_markup=kbs.picture_menu)
            await api.set_picture_category(self._user_id, self._category)

    async def _send_picture(self):
        photo_ids = self._picture

        if len(photo_ids) > 1:
            media = [types.InputMediaPhoto(i) for i in photo_ids]
            await self._message.answer_media_group(media)
        else:
            await self._message.answer_photo(photo_ids[0])
