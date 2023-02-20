from aiogram import types

import lib
from assets import kbs
from core import dp
from loader import api


@dp.click(kbs.PictureMenu.get_another)
async def _(msg: types.Message):
    category = await api.get_picture_category(msg.from_user.id)

    if not category:
        await lib.ask_to_restart_bot(msg)
        return

    await lib.on_picture_request(msg, category)


@dp.text('♻️ Хочу другую')
async def _(msg: types.Message):
    await lib.ask_to_restart_bot(msg)
