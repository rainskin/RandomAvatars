from assets import PictureCategory
from assets.keyboards import MainMenu
from core import *
from lib import PictureRequest


def pick_category(query: QUERY) -> PictureCategory | None:
    for button, category in _BUTTON_TO_CATEGORY:
        if query.data == button.data:
            return category


_BUTTON_TO_CATEGORY = [
    (MainMenu.anime_avatars, PictureCategory.AVATAR),
    (MainMenu.paired_avatars, PictureCategory.PAIRED_AVATARS),
    (MainMenu.cute_pictures, PictureCategory.CUTE),
    (MainMenu.angry_pictures, PictureCategory.ANGRY),
]


def on_picture_request(query: QUERY, category: PictureCategory):
    request = PictureRequest(
        query.from_user,
        query.message,
        category,
        require_keyboard=True,
    )
    return request.respond()
