from botty import (
    Message,
    Query,
    r,
)

from api import (
    get_picture_category,
    set_picture_category,
)
from assets import (
    PictureCategory,
    answers,
)
from lib import PictureRequest, on_picture_request


def send_picture(category: PictureCategory):
    async def callback(query: Query):
        request = PictureRequest(query.from_user, query.message)
        if await request.respond(category):
            await r(query, answers.picture_menu)
            set_picture_category(query.from_user.id, category)

    return callback


def send_another_picture(msg: Message):
    category = get_picture_category(msg.from_user.id)
    return on_picture_request(msg, category)


def send_menu(msg: Message):
    return r(msg, answers.start(msg))
