import httpx

from assets import PictureCategory

JSON = dict | list | int | bool


class Api:
    def __init__(self, base_url: str):
        self._base_url = base_url
        self._client = httpx.AsyncClient()

    async def _get(self, endpoint: str, params: dict = None) -> JSON:
        url = self._base_url + endpoint
        resp = await self._client.get(url, params=params)
        return resp.json()

    async def _set(self, endpoint: str, params: dict = None) -> JSON:
        url = self._base_url + endpoint
        resp = await self._client.post(url, params=params)
        return resp.json()

    async def get_picture(self, category: PictureCategory, chat_id: int) -> list[str]:
        endpoint = f'/picture/{category}'
        params = {'chat_id': chat_id}
        result = await self._get(endpoint, params)
        return result

    async def get_cooldown(self, user_id: int, chat_type: str) -> int:
        endpoint = f'/cooldown/{user_id}'
        params = {'chat_type': chat_type}
        result = await self._get(endpoint, params)
        return result['remaining_time']

    async def set_cooldown(self, user_id: int) -> bool:
        endpoint = f'/cooldown/{user_id}'
        result = await self._set(endpoint)
        return result['ok']

    async def get_picture_category(self, user_id: int) -> PictureCategory:
        endpoint = f'/picture-category/{user_id}'
        result = await self._get(endpoint)
        return result['category']

    async def set_picture_category(self, category: PictureCategory, user_id: int) -> bool:
        endpoint = f'/picture-category/{user_id}'
        params = {'category': category}
        result = await self._set(endpoint, params)
        return result['ok']

    async def get_chats(self) -> list[int]:
        endpoint = f'/chats'
        result = await self._get(endpoint)
        return result
