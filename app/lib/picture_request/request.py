from botty import Message, User, r, obtain_invite_link

import answers
from api import PictureCategory, get_cooldown, get_picture
from lib.helpers import save_chat
from .required_join import RequiredJoin
from .response import Response


def on_picture_request(msg: Message, category: PictureCategory):
    request = PictureRequest(msg.from_user, msg)
    return request.respond(category)


class PictureRequest:
    _picture: list[str] = None

    def __init__(
        self,
        user: User,
        message: Message,
    ):
        self._user_id = user.id
        self._message = message
        self._chat = self._message.chat

    async def respond(self, category: PictureCategory) -> bool:
        save_chat(self._message)

        if chat_id := await RequiredJoin(self._chat, self._user_id).get_chat_id():
            await self._ask_to_join_chat(chat_id)
            return False

        if cooldown := get_cooldown(self._user_id, self._chat.type):
            await self._ask_wait(cooldown)
            return False

        picture = get_picture(category, self._chat.id)
        resp = Response(picture, self._message, self._user_id)
        return await resp.send()

    async def _ask_to_join_chat(self, chat_id: int):
        invite_link = await obtain_invite_link(chat_id)
        await r(self._message, answers.join_required(invite_link))

    def _ask_wait(self, cooldown: int):
        return r(self._message, answers.wait_for(cooldown), quote=True)
