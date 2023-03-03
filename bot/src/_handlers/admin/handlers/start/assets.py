from core import dp

import config
from assets import commands
from ... import assets as admin

event = dp.command(commands.ADMIN, user_id=config.ADMIN_IDS)
text = admin.menu_text
keyboard = admin.main_keyboard
