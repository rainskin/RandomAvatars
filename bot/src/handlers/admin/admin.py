import lib


@lib.events.admin.command
async def _(msg: lib.MESSAGE):
    await lib.answers.admin_panel(msg)
