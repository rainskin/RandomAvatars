from core import BaseApi


class Cooldown(BaseApi):

    def get(self, chat_type: str) -> int:
        return self._get(
            params={'chat_type': chat_type},
        )

    def set(self) -> bool:
        return self._set()
