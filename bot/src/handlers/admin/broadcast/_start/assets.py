from core import dp
from lib import States, kbs

event = dp.click(kbs.AdminPanel.broadcast)
state = States.broadcast
text = 'Жду пост, давай только без альбомов'
keyboard = kbs.admin_cancel
