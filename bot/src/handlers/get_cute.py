from aiogram import types

import lib
from assets import commands, PictureCategory
from core import dp


@dp.command(commands.GET_CUTE)
async def _(msg: types.Message):
    await lib.on_picture_request(msg, PictureCategory.CUTE)
