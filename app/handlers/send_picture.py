from botty import dp, Message, r

import answers
from api import Command


@dp.command(Command.SEND_PICTURE)
def _(msg: Message):
    return r(msg, answers.DOES_NOT_WORK)
