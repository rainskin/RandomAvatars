import lib


@lib.events.admin.post_from_channel
async def _(msg: lib.MESSAGE):
    await lib.answers.on_post_from_channel(msg)
