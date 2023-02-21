import lib


@lib.events.send_picture
async def _(msg: lib.MESSAGE):
    await lib.answers.does_not_work(msg)
