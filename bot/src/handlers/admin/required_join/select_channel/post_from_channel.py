from lib import *


@events.admin.post_from_channel
async def _(msg: MESSAGE):
    await answers.on_post_from_channel(msg)
