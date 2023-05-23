from botty import Chat, TelegramAPIError, bot, is_private

from api import get_required_join_chat


class RequiredJoin:
    def __init__(self, chat: Chat, user_id: int) -> None:
        self._chat = chat
        self._user_id = user_id

    async def get_chat_id(self) -> int | None:
        if not is_private(self._chat):
            return None

        if not (chat_id := get_required_join_chat()):
            return None

        if not await self._joined(chat_id):
            return chat_id
        return None

    async def _joined(self, chat_id: int) -> bool:
        try:
            chat_member = await bot.get_chat_member(chat_id, self._user_id)
        except TelegramAPIError:
            return False

        return chat_member.is_chat_member()
