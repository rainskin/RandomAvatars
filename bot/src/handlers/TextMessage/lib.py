import config
from assets import PictureCategory
from core import *


def pick_category(msg: MESSAGE) -> PictureCategory | None:
    words = msg.text.lower().split()

    for word in words:
        for triggers, category in _TRIGGERS_TO_CATEGORY:
            if word in triggers:
                return category


_TRIGGERS_TO_CATEGORY = [
    (config.TriggerWords.avatar, PictureCategory.AVATAR),
    (config.TriggerWords.paired_avatars, PictureCategory.PAIRED_AVATARS),
    (config.TriggerWords.cute_picture, PictureCategory.CUTE),
    (config.TriggerWords.angry_picture, PictureCategory.ANGRY),
]
