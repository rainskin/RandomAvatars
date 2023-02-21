from aiogram import types

import lib


@lib.events.text
async def _(msg: types.Message):
    if category := lib.choose_picture_category(msg):
        await lib.on_picture_request(msg, category)
