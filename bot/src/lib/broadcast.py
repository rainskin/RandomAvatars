import asyncio

from aiogram.utils.exceptions import RetryAfter, TelegramAPIError

from .assets import texts
from lib.loader import api
from .consts import *


class Broadcast:

    def __init__(self, post: MESSAGE):
        self._loop = asyncio.get_running_loop()
        self._post = post
        self._delivered_count = 0
        self._floods_count = 0
        self._errors_count = 0

    def schedule(self):
        self._loop.create_task(self._broadcast())

    async def _broadcast(self):
        chat_ids = await api.get_chats()

        for i in chat_ids:
            await self._try_copy_post(i)

        await self._send_summary()

    async def _try_copy_post(self, chat_id: int):
        try:
            await self._post.copy_to(chat_id)
        except RetryAfter as e:
            self._floods_count += 1
            await asyncio.sleep(e.timeout)
        except TelegramAPIError:
            self._errors_count += 1
        else:
            self._delivered_count += 1
        finally:
            await asyncio.sleep(0.1)

    def _send_summary(self):
        return self._post.answer(self._get_summary())

    def _get_summary(self) -> str:
        return texts.broadcast_summary.format(
            delivered_count=self._delivered_count,
            floods_count=self._floods_count,
            errors_count=self._errors_count,
        )
