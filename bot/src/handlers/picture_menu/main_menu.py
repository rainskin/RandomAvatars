from aiogram import types

import lib


@lib.events.picture_menu.main_menu
async def _(msg: types.Message):
    await lib.answers.main_menu(msg)
