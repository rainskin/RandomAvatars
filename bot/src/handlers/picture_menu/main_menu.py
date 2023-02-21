from aiogram import types

import lib
from assets import kbs
from core import dp


@dp.click(kbs.PictureMenu.main_menu)
async def _(msg: types.Message):
    await lib.answers.main_menu(msg)
