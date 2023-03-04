from core import *
from handlers.Admin import assets as admin
from ... import assets as required_joins

event = dp.click(required_joins.keyboard.select_channel)
state = State(__name__)
text = 'Пришли мне любой пост из канала'
keyboard = admin.cancel_keyboard
