from assets import PictureCategory
from core import *
from lib import PictureRequest, api
from . import assets


def pick_category(query: QUERY) -> PictureCategory | None:
    for button, category in assets.BUTTON_TO_CATEGORY:
        if query.data == button.data:
            return category


async def on_picture_request(query: QUERY, category: PictureCategory):
    request = PictureRequest(query.from_user, query.message)
    if await request.respond(category):
        await utils.answer(query.message, assets.text, assets.picture_menu)
        await api.user(query.from_user.id).picture_category.set(category)
