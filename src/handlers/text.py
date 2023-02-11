from aiogram import types

import config
import lib
from assets import PictureCategory
from core import dp


@dp.text()
async def _(msg: types.Message):
    text_words = msg.text.split()
    picture_category = None

    triggers_to_category = [
        (config.TextTriggers.AVATAR, PictureCategory.AVATAR),
        (config.TextTriggers.PAIRED_AVATARS, PictureCategory.PAIRED_AVATARS),
        (config.TextTriggers.CUTE_PICTURE, PictureCategory.CUTE),
        (config.TextTriggers.ANGRY_PICTURE, PictureCategory.ANGRY),
    ]

    for _triggers, _category in triggers_to_category:
        if contain_any_word(_triggers, text_words):
            picture_category = _category

    if picture_category:
        await lib.on_picture_request(msg, picture_category)


def contain_any_word(search_words: list[str], text_words: list[str]) -> bool:
    for sw in search_words:
        if sw in text_words:
            return True
    return False
