from botty import Chat, TelegramAPIError, bot, is_private

import api


class RequiredJoin:
    def __init__(self, chat: Chat, user_id: int) -> None:
        self._chat = chat
        self._user_id = user_id

    async def get_joins(self) -> list[api.RequiredJoin]:
        if not is_private(self._chat):
            return []

        if not (joins := api.RequiredJoin.find_all()):
            return []

        if not await self._joined(joins):
            return joins
        return []

    async def _joined(self, joins: list[api.RequiredJoin]) -> bool:
        try:
            for j in joins:
                chat_member = await bot.get_chat_member(j.chat_id, self._user_id)
                if not chat_member.is_chat_member():
                    return False
        except TelegramAPIError:
            return False
        return True
