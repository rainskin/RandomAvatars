from core import BaseHandler, utils

from lib import api
from .assets import keyboard


class Handler(BaseHandler):

    async def callback(self):
        text = await get_text()
        await self.answer(text, keyboard)


async def get_text():
    chat_id = await api.required_join.get_chat_id()

    if not chat_id:
        return 'Обязательная подписка отключена'

    invite_link = await utils.get_invite_link(chat_id)
    return f'Обязательная подписка: {invite_link}'
