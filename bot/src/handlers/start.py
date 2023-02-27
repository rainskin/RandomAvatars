from lib import *


@events.start
async def _(msg: MESSAGE):
    await utils.reset_state()
    await answers.start(msg)

    if utils.is_admin(msg.from_user):
        await utils.update_my_commands()

    await utils.save_chat(msg.chat)
