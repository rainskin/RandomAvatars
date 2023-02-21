import lib


@lib.events.admin.broadcast_post
async def _(msg: lib.MESSAGE):
    await lib.reset_state()
    await lib.answers.broadcast_started(msg)
    lib.schedule_broadcast(msg)
