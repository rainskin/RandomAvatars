import random
import time

from aiogram import types
from aiogram.utils.deep_linking import get_startgroup_link
from aiogram.utils.exceptions import WrongFileIdentifier

import config
import database
from assets import PictureCategory, texts, kbs
from loader import db, logger


async def on_picture_request(update: types.Message | types.CallbackQuery, category: PictureCategory):
    photo_ids = get_random_picture(category)
    send_picture_menu = False
    user = update.from_user
    user_doc = db.get_user(user.id)

    if isinstance(update, types.CallbackQuery):
        msg = update.message
        send_picture_menu = True
        user_doc.save_picture_category(category)
        await update.answer()
    else:
        msg = update

    remaining_cooldown = get_remaining_cooldown(user_doc)

    if msg.chat.type != 'private' and remaining_cooldown:
        await msg.answer(texts.wait_for.format(time=remaining_cooldown))
        return

    try:
        await answer_picture(msg, photo_ids)
    except WrongFileIdentifier:
        logger.error(f'WrongFileIdentifier: {photo_ids}')
        return

    user_doc.save_last_request_time(time.time())

    if send_picture_menu:
        kb = kbs.PictureMenu().create()
        await msg.answer(texts.picture_menu_hint, reply_markup=kb)


def get_random_picture(category: PictureCategory) -> list[str]:
    pictures = db.get_pictures(category)
    picture = random.choice(pictures)
    return picture.photo_ids


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


def get_remaining_cooldown(user: database.User) -> int:
    delta = int(time.time() - user.last_request_time)
    return max(0, config.REQUEST_COOLDOWN - delta)
