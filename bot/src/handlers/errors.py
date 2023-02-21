from contextlib import suppress

from aiogram import types
from aiogram.utils.exceptions import BadRequest

import lib
from assets import texts


@lib.events.bad_request
async def _(update: types.Update, exc: BadRequest):
    error_desc = exc.args[0]
    msg = update.message or update.callback_query.message

    if error_desc == 'Not enough rights to send photos to the chat':
        with suppress(BadRequest):
            await msg.answer(texts.no_send_photo_rights)
        return True
    elif error_desc == 'Not enough rights to send text messages to the chat':
        return True
