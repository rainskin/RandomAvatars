from lib import *


@events.admin.broadcast_post
async def _(msg: MESSAGE):
    await utils.reset_state()
    await answers.broadcast_started(msg)
    broadcast.schedule(msg)
