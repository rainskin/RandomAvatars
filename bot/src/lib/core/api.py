import httpx

RESULT = dict | list | int | bool


class BaseApi:
    def __init__(self, base_url: str):
        self._base_url = base_url
        self._client = httpx.AsyncClient()

    def _get(self, endpoint: str, params: dict = None):
        return self._request('GET', endpoint, params)

    def _set(self, endpoint: str, params: dict = None, json: dict = None):
        return self._request('POST', endpoint, params, json)

    def _delete(self, endpoint: str, params: dict = None):
        return self._request('DELETE', endpoint, params)

    async def _request(
            self, method: str,
            endpoint: str,
            params: dict = None,
            json: dict = None,
    ) -> RESULT:
        url = self._base_url + endpoint
        resp = await self._client.request(method, url, params=params, json=json)
        return get_result(resp)


def get_result(response: httpx.Response) -> RESULT:
    json = response.json()
    return json['result']
