from contextlib import suppress

from botty import dp, Update, NoSendTextRights, NoSendPhotoRights, r

import answers


@dp.error(NoSendPhotoRights)
async def _(upd: Update, _):
    await ask_rights(upd)
    return True


async def ask_rights(upd: Update):
    if not (event := upd.message or upd.callback_query):
        return
    with suppress(NoSendTextRights):
        await r(event, answers.ASK_RIGHTS)
