from core import dp
from lib import kbs

event = dp.click(kbs.ADMIN_BACK_BUTTON, state='*')
text = 'Вот твоя админ-панель, хозяин 🥵'
keyboard = kbs.admin_panel
