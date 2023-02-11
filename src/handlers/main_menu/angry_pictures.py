from aiogram import types

import lib
from assets import PictureCategory, kbs
from core import dp


@dp.click(kbs.MainMenu.angry_pictures)
async def _(query: types.CallbackQuery):
    await lib.answer_random_picture(query, PictureCategory.ANGRY)
