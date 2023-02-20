from enum import Enum


class PictureCategory(str, Enum):
    AVATAR = 'avatar'
    PAIRED_AVATARS = 'paired_avatars'
    CUTE = 'cute'
    ANGRY = 'angry'
