import config
from core import dp
from lib import commands, kbs

event = dp.command(commands.ADMIN, user_id=config.ADMIN_IDS)
text = 'Вот твоя админ-панель, хозяин 🥵'
keyboard = kbs.admin_panel
