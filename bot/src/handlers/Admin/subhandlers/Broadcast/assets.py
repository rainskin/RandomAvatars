from core import *

from handlers.Admin import assets as admin

event = dp.click(admin.main_keyboard.broadcast)
state = State(__name__)
text = 'Жду пост, давай только без альбомов'
keyboard = admin.cancel_keyboard
