from core import dp

from assets import STATES
from handlers.admin import assets as admin
from ..... import assets as required_joins

event = dp.click(required_joins.keyboard.select_channel)
state = STATES.required_join
text = 'Пришли мне любой пост из канала'
keyboard = admin.cancel_keyboard
