import random
import time
from typing import cast

from assets import config
from assets.types import PictureCategory

from .database import db, models


def get_picture(category: PictureCategory, chat_id: int) -> list[str]:
    pictures = db.get_pictures(category, chat_id)
    picture: models.Picture = random.choice(pictures)
    db.save_sent_picture(chat_id, picture)
    return picture.photo_ids


def get_cooldown(user_id: int, chat_type: str) -> int:
    user = db.get_user(user_id)

    delta = int(time.time() - user.last_request_time)
    remaining_time = max(0, config.PICTURE_REQUEST_COOLDOWN - delta)

    if chat_type == "private":
        remaining_time = 0

    return remaining_time


def set_cooldown(user_id: int):
    user = db.get_user(user_id)
    user.save_last_request_time(time.time())


def get_picture_category(user_id: int) -> PictureCategory:
    user = db.get_user(user_id)
    return cast(PictureCategory, user.picture_category)


def set_picture_category(user_id: int, category: PictureCategory):
    user = db.get_user(user_id)
    user.save_picture_category(category)


def get_chats() -> list[int]:
    return [c.id for c in db.get_chats()]  # type: ignore[reportGeneralTypeIssues]


def save_chat(chat_id: int, utm: str | None = None):
    db.save_chat(chat_id, utm or None)


def get_utm():
    counter: dict[str, int] = {}
    for c in db.get_chats():
        if c.utm:
            counter[c.utm] = counter.get(c.utm, 0) + 1
    return counter
