from aiogram import types
from aiogram.utils.exceptions import BadRequest

from assets import texts
from core import dp


@dp.errors_handler(exception=BadRequest)
async def _(update: types.Update, exc: BadRequest):
    error_desc = exc.args[0]
    msg = update.message or update.callback_query.message

    if error_desc == 'Not enough rights to send photos to the chat':
        await msg.answer(texts.no_send_photo_rights)
        return True
    elif error_desc == 'Not enough rights to send text messages to the chat':
        return True
