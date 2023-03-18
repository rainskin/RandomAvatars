from lib import commands
from lib.assets import PictureCategory

CATEGORY_BY_TRIGGER = {
    commands.GET_AVATARS: PictureCategory.AVATAR,
    commands.GET_PAIRED: PictureCategory.PAIRED_AVATARS,
    commands.GET_CUTE: PictureCategory.CUTE,
    commands.GET_ANGRY: PictureCategory.ANGRY,
}
