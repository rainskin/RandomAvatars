from assets import PictureCategory
from core import *
from lib import PictureRequest
from .assets import COMMAND_TO_CATEGORY


def on_picture_request(msg: MESSAGE, category: PictureCategory):
    request = PictureRequest(msg.from_user, msg, category)
    return request.respond()


def pick_category(msg: MESSAGE) -> PictureCategory:
    command = msg.get_command(pure=True)
    return COMMAND_TO_CATEGORY[command]
