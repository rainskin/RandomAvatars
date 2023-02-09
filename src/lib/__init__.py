from aiogram import types

import config
from assets import PictureCategory


async def answer_random_picture(msg: types.Message, category: PictureCategory):
    photo_ids = get_random_picture(category)
    await answer_picture(msg, photo_ids)


def get_random_picture(category: PictureCategory) -> list[str]:
    match category:
        case PictureCategory.AVATAR:
            return ['https://telegra.ph/file/38155954f1b1e04a554f3.jpg']
        case PictureCategory.PAIRED:
            return ['https://telegra.ph/file/cdcca12410a6747e2fd5d.jpg',
                    'https://telegra.ph/file/711497c34cb1a6806d304.jpg']
        case PictureCategory.CUTE:
            return ['https://telegra.ph/file/cce011a5205d6c3007bfe.jpg']
        case PictureCategory.ANGRY:
            return ['https://telegra.ph/file/ed333fa6b8f39620c759e.jpg']


async def answer_picture(msg: types.Message, photo_ids: list[str]):
    if len(photo_ids) > 1:
        media = [types.InputMediaPhoto(i) for i in photo_ids]
        await msg.answer_media_group(media)
    else:
        await msg.answer_photo(photo_ids[0])


def is_admin(user: types.User) -> bool:
    return user.id in config.ADMIN_IDS
