from lib import *


@events.bad_request
async def _(update: UPDATE, exc: Exception):
    error_desc = exc.args[0]

    if error_desc == 'Not enough rights to send photos to the chat':
        await answers.no_send_photo_rights(update)
        return True
    if error_desc == 'Not enough rights to send text messages to the chat':
        return True
