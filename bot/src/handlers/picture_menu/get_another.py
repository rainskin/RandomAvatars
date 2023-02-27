from lib import *


@events.picture_menu.get_another
async def _(msg: MESSAGE):
    category = await utils.get_picture_category(msg.from_user)

    if not category:
        return await answers.ask_to_restart_bot(msg)

    await answers.requests.respond_picture(msg, category)


@events.picture_menu.old_get_another
async def _(msg: MESSAGE):
    await answers.ask_to_restart_bot(msg)
