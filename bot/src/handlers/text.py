from lib import *


@events.text
async def _(msg: MESSAGE):
    await answers.requests.respond(msg)
