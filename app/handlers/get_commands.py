from botty import Message, dp

from api import PictureCategory, Command
from lib import on_picture_request

COMMAND_TO_CATEGORY = {
    Command.GET_AVATARS: PictureCategory.AVATAR,
    Command.GET_PAIRED: PictureCategory.PAIRED_AVATARS,
    Command.GET_CUTE: PictureCategory.CUTE,
    Command.GET_ANGRY: PictureCategory.ANGRY,
}


@dp.command(list(COMMAND_TO_CATEGORY))
async def _(msg: Message):
    if category := pick_category(msg):
        await on_picture_request(msg, category)


def pick_category(msg: Message) -> PictureCategory:
    command = msg.get_command(pure=True)
    return COMMAND_TO_CATEGORY[command]
