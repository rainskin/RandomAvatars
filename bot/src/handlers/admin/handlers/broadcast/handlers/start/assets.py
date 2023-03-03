from core import dp

from assets import STATES
from handlers.admin import assets as admin

event = dp.click(admin.main_keyboard.broadcast)
state = STATES.broadcast
text = 'Жду пост, давай только без альбомов'
keyboard = admin.cancel_keyboard
