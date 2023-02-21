import lib


@lib.events.picture_menu.get_another
async def _(msg: lib.MESSAGE):
    category = await lib.get_picture_category(msg.from_user)

    if not category:
        await lib.answers.ask_to_restart_bot(msg)
        return

    await lib.on_picture_request(msg, category)


@lib.events.picture_menu.old_get_another
async def _(msg: lib.MESSAGE):
    await lib.answers.ask_to_restart_bot(msg)
