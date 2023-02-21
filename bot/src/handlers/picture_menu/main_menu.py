import lib


@lib.events.picture_menu.main_menu
async def _(msg: lib.MESSAGE):
    await lib.answers.main_menu(msg)
