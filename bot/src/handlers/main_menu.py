from aiogram import types

import lib


@lib.events.main_menu.get_picture
async def _(query: types.CallbackQuery):
    if category := lib.choose_picture_category(query):
        await lib.on_picture_request(query, category)
