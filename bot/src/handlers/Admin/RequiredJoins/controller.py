from core import *
from lib import api

from .assets import keyboard, Texts


class Controller(BaseController):

    async def callback(self):
        text = await get_text()
        await self.answer(text, keyboard)


async def get_text():
    chat_id = await api.required_join.get_chat_id()

    if not chat_id:
        return Texts.disabled

    invite_link = await utils.get_invite_link(chat_id)
    return Texts.info.format(invite_link)
