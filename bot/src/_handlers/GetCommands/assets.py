from assets import commands, PictureCategory
from core import *

COMMAND_TO_CATEGORY = {
    commands.GET_AVATARS: PictureCategory.AVATAR,
    commands.GET_PAIRED: PictureCategory.PAIRED_AVATARS,
    commands.GET_CUTE: PictureCategory.CUTE,
    commands.GET_ANGRY: PictureCategory.ANGRY,
}

event = dp.command(list(COMMAND_TO_CATEGORY))
