from aiogram import types
from aiogram.utils.deep_linking import get_startgroup_link

import config
from assets import PictureCategory, texts, kbs


async def on_picture_request(update: types.Message | types.CallbackQuery, category: PictureCategory):
    photo_ids = get_random_picture(category)

    if isinstance(update, types.CallbackQuery):
        msg = update.message
        await answer_picture(msg, photo_ids)
        kb = kbs.PictureMenu().create()
        await msg.answer(texts.picture_menu_hint, reply_markup=kb)
    else:
        msg = update
        await answer_picture(msg, photo_ids)


def get_random_picture(category: PictureCategory) -> list[str]:
    match category:
        case PictureCategory.AVATAR:
            return ['https://telegra.ph/file/38155954f1b1e04a554f3.jpg']
        case PictureCategory.PAIRED_AVATARS:
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


async def answer_main_menu(msg: types.Message):
    text = texts.welcome.format(mention=msg.from_user.get_mention())
    startgroup_url = await get_startgroup_link('0')
    kb = kbs.MainMenu(startgroup_url).create()
    await msg.answer(text, reply_markup=kb)
