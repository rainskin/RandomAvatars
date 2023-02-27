import asyncio
from dataclasses import dataclass

from aiogram.utils.exceptions import RetryAfter, TelegramAPIError

from lib.assets import texts
from core.constants import *
from lib.loader import api


class Broadcast:
    INTERVAL = 0.1

    def __init__(self, post: MESSAGE):
        self._loop = asyncio.get_running_loop()
        self._post = post
        self._message_count = MessageCount()

    def schedule(self):
        self._loop.create_task(self._broadcast())

    async def _broadcast(self):
        chat_ids = await api.chats.get()

        for i in chat_ids:
            await self._try_copy_post(i)

        await self._send_summary()

    async def _try_copy_post(self, chat_id: int):
        try:
            await self._post.copy_to(chat_id)
        except RetryAfter as e:
            self._message_count.floods += 1
            await asyncio.sleep(e.timeout)
        except TelegramAPIError:
            self._message_count.errors += 1
        else:
            self._message_count.delivered += 1
        finally:
            await asyncio.sleep(self.INTERVAL)

    def _send_summary(self):
        return self._post.answer(self._message_count.summary)


@dataclass
class MessageCount:
    delivered: int = 0
    floods: int = 0
    errors: int = 0

    @property
    def summary(self) -> str:
        return texts.broadcast_summary.format(
            delivered_count=self.delivered,
            floods_count=self.floods,
            errors_count=self.errors,
        )
