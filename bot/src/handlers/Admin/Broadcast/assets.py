from lib.Admin.assets import MenuKeyboard, cancel_keyboard

event = dp.click(MenuKeyboard.broadcast)
post_state = State(__name__)
text = 'Жду пост, давай только без альбомов'
keyboard = cancel_keyboard
