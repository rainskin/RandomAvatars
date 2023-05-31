from botty import Message, User, r

import api
from api import get_cooldown, get_picture
from assets import PictureCategory, answers
from lib.helpers import save_chat

from .required_join import RequiredJoin
from .response import Response


def on_picture_request(msg: Message, category: PictureCategory):
    request = PictureRequest(msg.from_user, msg)
    return request.respond(category)


class PictureRequest:
    _picture: list[str] | None = None

    def __init__(
        self,
        user: User,
        message: Message,
    ) -> None:
        self._user_id = user.id
        self._message = message
        self._chat = self._message.chat

    async def respond(self, category: PictureCategory) -> bool:
        picture = await self.fetch_picture(category)
        if not picture:
            return False
        resp = Response(picture, self._message, self._user_id)
        return await resp.send()

    async def fetch_picture(self, category: PictureCategory):
        save_chat(self._message)
        if joins := await RequiredJoin(self._chat, self._user_id).get_joins():
            await self._ask_to_join_chats(joins)
            return False
        if cooldown := get_cooldown(self._user_id, self._chat.type):
            await self._ask_wait(cooldown)
            return False
        return get_picture(category, self._chat.id)

    async def _ask_to_join_chats(self, joins: list[api.RequiredJoin]):
        links = [j.link for j in joins]
        await r(self._message, answers.join_required(links))

    def _ask_wait(self, cooldown: int):
        return r(self._message, answers.wait_for(cooldown), quote=True)
