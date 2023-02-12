from aiogram import types

import lib
from assets import kbs
from core import dp
from loader import db


@dp.click(kbs.PictureMenu.get_another)
async def _(msg: types.Message):
    picture_category = db.get_user(msg.from_user.id).picture_category
    await lib.on_picture_request(msg, picture_category)
