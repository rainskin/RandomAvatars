from core import BaseApi


class Chats(BaseApi):

    def get(self) -> list[int]:
        return self._get()

    def save(self, chat_id: int, utm: str = None) -> bool:
        return self._set(
            endpoint=f'/{chat_id}',
            params={'utm': utm}
        )
