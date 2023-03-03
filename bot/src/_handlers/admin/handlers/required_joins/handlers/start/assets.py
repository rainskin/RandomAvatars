from core import dp

from handlers.admin import assets as admin
from ... import assets as required_join

event = dp.click(admin.main_keyboard.required_join)
keyboard = required_join.keyboard
