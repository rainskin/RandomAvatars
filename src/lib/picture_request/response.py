from aiogram.types import InputMediaPhoto
from botty import Message

from api import set_cooldown
from lib.helpers import get_random_sign


class Response:
    def __init__(
        self,
        picture: list[str],
        message: Message,
        user_id: int,
    ) -> None:
        self._picture = picture
        self._message = message
        self._user_id = user_id

    async def send(self) -> bool:
        await self._send_picture()
        set_cooldown(self._user_id)
        return True

    async def _send_picture(self):
        photo_ids = self._picture
        sign = get_random_sign()
        await answer_picture(self._message, photo_ids, sign)


async def answer_picture(msg: Message, photo_ids: list[str], sign: str | None = None):
    if len(photo_ids) > 1:
        media = [InputMediaPhoto(i) for i in photo_ids]
        media[0].caption = sign
        await msg.answer_media_group(media)  # type: ignore[TODO]
    else:
        await msg.answer_photo(photo_ids[0], sign)
