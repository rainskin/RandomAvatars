from core import BaseApi


class Pictures(BaseApi):

    def get_random(self, chat_id: int) -> list[str]:
        return self._get(
            params={'chat_id': chat_id},
        )
