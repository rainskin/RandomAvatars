from enum import Enum


class PictureCategory(str, Enum):
    AVATAR = 'avatar'
    PAIRED = 'paired'
    CUTE = 'cute'
    ANGRY = 'angry'
