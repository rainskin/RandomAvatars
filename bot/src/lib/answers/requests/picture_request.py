from aiogram import types
from aiogram.types import ChatType
from aiogram.utils.exceptions import TelegramAPIError
from core import bot
from core.answers import answer
from core.constants import *
from core.utils import get_invite_link

from assets import keyboards
from lib.api import api
from lib.assets import texts, PictureCategory
from lib.utils import save_chat


class PictureRequest:
    _picture: list[str] = None

    def __init__(self, request: REQUEST, category: PictureCategory):
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
        required_join_chat_id = await self._get_required_join_chat_id()
        cooldown = await api.user(self._user_id).cooldown.get(self._chat.type)
        await save_chat(self._chat)

        if required_join_chat_id:
            invite_link = await get_invite_link(required_join_chat_id)
            text = texts.ask_to_join_chat.format(invite_link=invite_link)
            await self._message.answer(text)
            return

        if cooldown:
            await self._ask_wait(cooldown)
            return

        picture = await api.pictures(self._category).get_random(self._chat.id)

        resp = Response(
            picture,
            self._message,
            self._user_id,
            self._category,
            self._require_keyboard,
        )
        await resp.send()

    def _ask_wait(self, cooldown: int):
        text = texts.wait_for.format(time=cooldown)
        return self._message.answer(text, reply=True)

    async def _get_required_join_chat_id(self) -> int | None:
        if self._chat.type != ChatType.PRIVATE:
            return None

        required_chat_id = await api.required_join.get_chat_id()

        if not required_chat_id:
            return None

        try:
            chat_member = await bot.get_chat_member(required_chat_id, self._user_id)
        except TelegramAPIError:
            return required_chat_id

        if not chat_member.is_chat_member():
            return required_chat_id


class Response:
    def __init__(self, picture: list[str], message: MESSAGE, user_id: int, category: PictureCategory,
                 require_keyboard: bool):
        self._picture = picture
        self._category = category
        self._require_keyboard = require_keyboard
        self._user_id = user_id
        self._message = message

    async def send(self):
        await self._send_picture()
        await api.user(self._user_id).cooldown.set()

        if self._require_keyboard:
            await answer(self._message, texts.picture_menu_hint, keyboards.picture_menu)
            await api.user(self._user_id).picture_category.set(self._category)

    async def _send_picture(self):
        photo_ids = self._picture

        if len(photo_ids) > 1:
            media = [types.InputMediaPhoto(i) for i in photo_ids]
            await self._message.answer_media_group(media)
        else:
            await self._message.answer_photo(photo_ids[0])
