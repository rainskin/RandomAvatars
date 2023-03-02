from aiogram.utils.exceptions import BadRequest

from core import dp
from lib.assets import commands
from . import main_menu, picture_menu

start = dp.command(commands.START, state='*')
text = dp.text()

send_picture = dp.command(commands.SEND_PICTURE)
bad_request = dp.errors_handler(exception=BadRequest)
