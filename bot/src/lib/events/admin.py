import config
from lib.assets import commands, States
from lib.assets import kbs
from lib.core import dp

back = dp.click(kbs.ADMIN_BACK_BUTTON, state='*')
command = dp.command(commands.ADMIN, user_id=config.ADMIN_IDS)
broadcast = dp.click(kbs.AdminPanel.broadcast)
broadcast_post = dp.any_message(state=States.broadcast)
post_from_channel = dp.any_message(state=States.required_join)
select_channel = dp.click(kbs.RequiredJoin.select_channel)
required_join_disable = dp.click(kbs.RequiredJoin.disable)
required_join = dp.click(kbs.AdminPanel.required_join)
