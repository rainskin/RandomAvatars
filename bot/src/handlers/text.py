from aiogram import types

import lib
from core import dp


@dp.text()
async def _(msg: types.Message):
    for triggers, category in lib.TRIGGERS_TO_CATEGORY:
        if lib.contain_trigger_words(msg.text, triggers):
            await lib.on_picture_request(msg, category)
            break
