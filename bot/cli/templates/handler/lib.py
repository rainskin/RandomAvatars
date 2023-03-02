import asyncio

from core import *


class Scheduler:

    def __init__(self, request: REQUEST):
        self._loop = asyncio.get_running_loop()
        self._request = request

    def schedule_answer(self, text: str, delay: int = 1):
        coro = delay_coro(self._answer(text), delay)
        self._loop.create_task(coro)

    async def _answer(self, text: str):
        await self._request.answer(text)


async def delay_coro(coro, delay: int):
    await asyncio.sleep(delay)
    await coro
