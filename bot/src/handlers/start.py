from lib import *


@events.start
async def _(msg: MESSAGE):
    await reset_state()
    await answers.start(msg)

    if is_admin(msg.from_user):
        await update_my_commands()

    await save_chat(msg.chat)
