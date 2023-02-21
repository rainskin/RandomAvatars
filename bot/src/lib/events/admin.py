import config
from assets import kbs, commands, States
from core import dp

back = dp.click(kbs.ADMIN_BACK_BUTTON, state='*')
command = dp.command(commands.ADMIN, user_id=config.ADMIN_IDS)
broadcast = dp.click(kbs.AdminPanel.broadcast)
broadcast_post = dp.any_message(state=States.broadcast)
