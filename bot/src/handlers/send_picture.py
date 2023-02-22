from lib import *


@events.send_picture
async def _(msg: MESSAGE):
    await answers.does_not_work(msg)
