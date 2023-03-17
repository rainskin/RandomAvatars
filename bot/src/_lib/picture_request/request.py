from assets import PictureCategory, texts
from .required_join import RequiredJoin
from .response import Response
from ..api import api
from ..utils import save_chat


def on_picture_request(msg: MESSAGE, category: PictureCategory):
    request = PictureRequest(msg.from_user, msg)
    return request.respond(category)


class PictureRequest:
    _picture: list[str] = None

    def __init__(
            self,
            user: USER,
            message: MESSAGE,
    ):
        self._user_id = user.id
        self._message = message
        self._chat = self._message.chat

    async def respond(self, category: PictureCategory) -> bool:
        await save_chat(self._chat)

        if chat_id := await RequiredJoin(self._chat, self._user_id).get_chat_id():
            await self._ask_to_join_chat(chat_id)
            return False

        if cooldown := await api.user(self._user_id).cooldown.get(self._chat.type):
            await self._ask_wait(cooldown)
            return False

        picture = await api.pictures(category).get_random(self._chat.id)
        resp = Response(picture, self._message, self._user_id)
        return await resp.send()

    async def _ask_to_join_chat(self, chat_id: int):
        invite_link = await utils.get_invite_link(chat_id)
        text = texts.ask_to_join_chat.format(invite_link)
        await self._message.answer(text)

    def _ask_wait(self, cooldown: int):
        text = texts.wait_for.format(cooldown)
        return self._message.answer(text, reply=True)
