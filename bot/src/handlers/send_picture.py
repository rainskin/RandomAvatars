from aiogram import types

import lib


@lib.events.send_picture
async def _(msg: types.Message):
    await lib.answers.does_not_work(msg)
