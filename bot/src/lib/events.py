from aiogram.utils.exceptions import BadRequest

from assets import commands
from core import dp

start = dp.command(commands.START, state='*')
text = dp.text()

_PICTURE_COMMANDS = [
    commands.GET_AVATARS,
    commands.GET_PAIRED,
    commands.GET_CUTE,
    commands.GET_ANGRY,
    commands.SEND_PICTURE,
]

get_picture = dp.command(_PICTURE_COMMANDS)
send_picture = dp.command(commands.SEND_PICTURE)
bad_request = dp.errors_handler(exception=BadRequest)
