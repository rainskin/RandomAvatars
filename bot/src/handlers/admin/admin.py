from lib import *


@events.admin.command
async def _(msg: MESSAGE):
    await answers.admin_panel(msg)
