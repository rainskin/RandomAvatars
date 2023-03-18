from config import TextTriggers
from lib.assets import PictureCategory

TRIGGERS_TO_CATEGORY = [
    (TextTriggers.AVATAR, PictureCategory.AVATAR),
    (TextTriggers.PAIRED_AVATARS, PictureCategory.PAIRED_AVATARS),
    (TextTriggers.CUTE_PICTURE, PictureCategory.CUTE),
    (TextTriggers.ANGRY_PICTURE, PictureCategory.ANGRY),
]
