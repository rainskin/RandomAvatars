import random

from botty import Message, User

import api
from api import Sign
from assets import ADMIN_IDS, PictureCategory, TriggerWords


def is_admin(user: User):
    return user.id in ADMIN_IDS


def save_chat(msg: Message):
    utm = msg.get_args() or None
    return api.save_chat(msg.chat.id, utm)


def get_random_sign() -> str | None:
    signs = [s.text for s in Sign.find_all()]
    return random.choice(signs) if signs else None


def pick_category(text: str) -> PictureCategory | None:
    words = text.lower().split()
    for word in words:
        for category, triggers in TRIGGERS_BY_CATEGORY.items():
            if word in triggers:
                return category
    return None


TRIGGERS_BY_CATEGORY: dict[PictureCategory, list[str]] = {
    "avatar": TriggerWords.avatar,
    "paired_avatars": TriggerWords.paired_avatars,
    "cute": TriggerWords.cute_picture,
    "angry": TriggerWords.angry_picture,
}
