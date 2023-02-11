from aiogram import types

import lib
from assets import kbs
from core import dp
from loader import db


@dp.click(kbs.PictureMenu.get_another)
async def _(msg: types.Message):
    picture_category = db.get_picture_category(msg.from_user.id)
    await lib.on_picture_request(msg, picture_category)
