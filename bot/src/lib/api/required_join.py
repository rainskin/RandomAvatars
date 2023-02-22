from core import BaseApi


class RequiredJoin(BaseApi):

    def get_chat_id(self) -> int:
        return self._get(
            endpoint=f'/chat',
        )

    def set_chat_id(self, chat_id: int | None) -> bool:
        return self._set(
            endpoint=f'/chat',
            json={'chat_id': chat_id},
        )
