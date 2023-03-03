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
    (config.TriggerWords.AVATAR, PictureCategory.AVATAR),
    (config.TriggerWords.PAIRED_AVATARS, PictureCategory.PAIRED_AVATARS),
    (config.TriggerWords.CUTE_PICTURE, PictureCategory.CUTE),
    (config.TriggerWords.ANGRY_PICTURE, PictureCategory.ANGRY),
]
