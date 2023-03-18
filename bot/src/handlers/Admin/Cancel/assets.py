from core import dp

from lib.Admin import assets as admin

event = dp.click(admin.BACK_BUTTON, state='*')
text = admin.text
keyboard = admin.main_keyboard
