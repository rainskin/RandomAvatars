from aiogram.utils.exceptions import BadRequest

from assets import commands
from core import dp
from . import main_menu, picture_menu, admin

start = dp.command(commands.START, state='*')
text = dp.text()

send_picture = dp.command(commands.SEND_PICTURE)
bad_request = dp.errors_handler(exception=BadRequest)
