from lib import *


@events.admin.broadcast_post
async def _(msg: MESSAGE):
    await reset_state()
    await answers.broadcast_started(msg)
    schedule_broadcast(msg)
