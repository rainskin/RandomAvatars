from lib import *


@events.picture_menu.main_menu
async def _(msg: MESSAGE):
    await answers.main_menu(msg)
