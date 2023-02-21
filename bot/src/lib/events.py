from assets import commands
from core import dp

start = dp.command(commands.START, state='*')
text = dp.text()
send_picture = dp.command(commands.SEND_PICTURE)
