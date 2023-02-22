from lib import *


@events.text
async def _(msg: MESSAGE):
    if category := choose_picture_category(msg):
        await on_picture_request(msg, category)
