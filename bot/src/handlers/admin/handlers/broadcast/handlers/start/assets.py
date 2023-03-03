from core import dp

from lib import States
from handlers.admin import assets as admin

event = dp.click(admin.main_keyboard.broadcast)
state = States.broadcast
text = 'Жду пост, давай только без альбомов'
keyboard = admin.cancel_keyboard
