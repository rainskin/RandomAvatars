from assets import PictureCategory
from core import *
from .assets import COMMAND_TO_CATEGORY


def pick_category(msg: MESSAGE) -> PictureCategory:
    command = msg.get_command(pure=True)
    return COMMAND_TO_CATEGORY[command]
