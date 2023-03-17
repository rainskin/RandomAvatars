from core import *

from ..assets import MainKeyboard, cancel_keyboard

event = dp.click(MainKeyboard.broadcast)
post_state = State(__name__)
text = 'Жду пост, давай только без альбомов'
keyboard = cancel_keyboard
