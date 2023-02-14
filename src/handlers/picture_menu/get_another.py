from aiogram import types

import lib
from assets import kbs
from core import dp
from loader import db


@dp.click(kbs.PictureMenu.get_another)
async def _(msg: types.Message):
    picture_category = db.get_user(msg.from_user.id).picture_category

    if not picture_category:
        await msg.answer('Пожалуйста, выбери категорию заново', reply_markup=kbs.removed)
        await lib.answer_main_menu(msg)
        return

    await lib.on_picture_request(msg, picture_category)


@dp.text('♻️ Хочу другую')
async def _(msg: types.Message):
    await lib.ask_to_restart_bot(msg)
