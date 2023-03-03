from lib import *


@events.text
async def _(msg: MESSAGE):
    await answers.requests.on_any_request(msg)
