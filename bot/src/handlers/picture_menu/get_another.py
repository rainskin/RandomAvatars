import lib
from lib import events, answers, MESSAGE


@events.picture_menu.get_another
async def _(msg: MESSAGE):
    category = await lib.get_picture_category(msg.from_user)

    if not category:
        return await answers.ask_to_restart_bot(msg)

    await lib.on_picture_request(msg, category)


@events.picture_menu.old_get_another
async def _(msg: MESSAGE):
    await answers.ask_to_restart_bot(msg)
