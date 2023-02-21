from aiogram import types

import lib


@lib.events.picture_menu.get_another
async def _(msg: types.Message):
    category = await lib.get_picture_category(msg.from_user)

    if not category:
        await lib.ask_to_restart_bot(msg)
        return

    await lib.on_picture_request(msg, category)


@lib.events.picture_menu.old_get_another
async def _(msg: types.Message):
    await lib.ask_to_restart_bot(msg)
