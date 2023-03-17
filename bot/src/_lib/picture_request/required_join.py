from core import *
from ..api import api


class RequiredJoin:
    def __init__(self, chat: CHAT, user_id: int):
        self._chat = chat
        self._user_id = user_id

    async def get_chat_id(self) -> int | None:
        if self._chat.type != CHAT_TYPES.PRIVATE:
            return None

        if not (chat_id := await api.required_join.get_chat_id()):
            return None

        if not await self._joined(chat_id):
            return chat_id

    async def _joined(self, chat_id: int) -> bool:
        try:
            chat_member = await bot.get_chat_member(chat_id, self._user_id)
        except TelegramAPIError:
            return False

        return chat_member.is_chat_member()
