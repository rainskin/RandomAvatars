from aiogram import types

import lib
from assets import commands, PictureCategory
from core import dp


@dp.command(commands.GET_ANGRY)
async def _(msg: types.Message):
    await lib.on_picture_request(msg, PictureCategory.ANGRY)
