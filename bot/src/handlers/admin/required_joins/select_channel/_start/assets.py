from core import dp
from lib import STATES, kbs

event = dp.click(kbs.RequiredJoin.select_channel)
state = STATES.required_join
text = 'Пришли мне любой пост из канала'
keyboard = kbs.admin_cancel
