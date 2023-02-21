from aiogram import types

import lib


@lib.events.start
async def _(msg: types.Message):
    await lib.reset_state()
    await lib.answers.start(msg)

    if lib.is_admin(msg.from_user):
        await lib.update_my_commands()

    await lib.save_chat(msg.chat)
