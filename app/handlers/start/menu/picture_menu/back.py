from botty import dp, Message, r

import answers
from assets import kbs


@dp.text(kbs.PictureMenu.BACK)
def _(msg: Message):
    return r(msg, answers.start(msg))
