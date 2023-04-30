from botty import dp, Message, r

import answers
from api import Command, ADMIN_IDS


@dp.command(Command.ADMIN).user_id(ADMIN_IDS)
def _(msg: Message):
    return r(msg, answers.ADMIN_MENU)
