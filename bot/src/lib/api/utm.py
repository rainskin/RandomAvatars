from core import BaseApi


class Utm(BaseApi):

    def get(self) -> list[int]:
        return self._get()
