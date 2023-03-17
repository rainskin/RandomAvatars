from core import *
from .. import assets as required_joins
from ... import assets as admin

event = dp.click(required_joins.keyboard.select_channel)
post_from_channel_state = State(__name__)
text = 'Пришли мне любой пост из канала'
keyboard = admin.cancel_keyboard
