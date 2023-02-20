import asyncio

from aiogram import types
from aiogram.utils.exceptions import RetryAfter, TelegramAPIError

from assets import texts
from loader import db


class Broadcast:

    def __init__(self, post: types.Message):
        self._loop = asyncio.get_running_loop()
        self._post = post
        self._delivered_count = 0
        self._floods_count = 0
        self._errors_count = 0

    def schedule(self):
        self._loop.create_task(self._broadcast())

    async def _broadcast(self):
        for chat in db.get_chats():
            await self._try_copy_post(chat.id)

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
