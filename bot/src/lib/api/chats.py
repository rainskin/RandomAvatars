from core import BaseApi


class Chats(BaseApi):

    def get(self) -> list[int]:
        return self._get()

    def save(self, chat_id: int) -> bool:
        return self._set(
            endpoint=f'/{chat_id}',
        )
