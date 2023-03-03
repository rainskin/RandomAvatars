from core import dp

from lib import States
from handlers.admin import assets as admin
from ..... import assets as required_joins

event = dp.click(required_joins.keyboard.select_channel)
state = States.required_join
text = 'Пришли мне любой пост из канала'
keyboard = admin.cancel_keyboard
