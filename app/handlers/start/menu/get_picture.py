from botty import Query, dp, r

import answers
from api import PictureCategory, set_picture_category
from assets import kbs
from lib import PictureRequest

CATEGORY_BY_BUTTON = {
    kbs.Menu.ANIME_AVATARS: PictureCategory.AVATAR,
    kbs.Menu.PAIRED_AVATARS: PictureCategory.PAIRED_AVATARS,
    kbs.Menu.CUTE_PICTURES: PictureCategory.CUTE,
    kbs.Menu.ANGRY_PICTURES: PictureCategory.ANGRY,
}


@dp.button(list(CATEGORY_BY_BUTTON))
async def _(query: Query):
    if category := pick_category(query):
        await on_picture_request(query, category)


def pick_category(query: Query) -> PictureCategory | None:
    for button, category in CATEGORY_BY_BUTTON.items():
        if query.data == button.callback_data:
            return category


async def on_picture_request(query: Query, category: PictureCategory):
    request = PictureRequest(query.from_user, query.message)
    if await request.respond(category):
        await r(query, answers.PICTURE_MENU)
        set_picture_category(query.from_user.id, category)
