from core import dp

from handlers.admin import assets as admin

event = dp.click(admin.BACK_BUTTON, state='*')
text = admin.menu_text
keyboard = admin.main_keyboard
