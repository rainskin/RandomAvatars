import httpx

from assets import PictureCategory


class Api:
    def __init__(self, base_url: str):
        self._base_url = base_url
        self._client = httpx.AsyncClient()

    async def _get(self, endpoint: str, params: dict = None) -> dict | list:
        url = self._base_url + endpoint
        resp = await self._client.get(url, params=params)
        return resp.json()

    async def get_picture(self, category: PictureCategory, chat_id: int) -> list[str]:
        endpoint = f'/picture/{category}'
        params = {'chat_id': chat_id}
        result = await self._get(endpoint, params)
        return result
