import httpx

from assets import PictureCategory


class Api:
    def __init__(self, base_url: str):
        self._base_url = base_url
        self._client = httpx.AsyncClient()

    async def _get(self, endpoint: str) -> dict | list:
        url = self._base_url + endpoint
        resp = await self._client.get(url)
        return resp.json()

    async def get_picture(self, category: PictureCategory) -> list[str]:
        endpoint = f'/picture/{category}'
        result = await self._get(endpoint)
        return result
