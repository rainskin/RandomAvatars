from aiogram import types

import lib
from assets import commands, PictureCategory
from core import dp


@dp.command(commands.GET_PAIRED)
async def _(msg: types.Message):
    await lib.answer_random_picture(msg, PictureCategory.PAIRED)
