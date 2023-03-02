from core import dp
from lib import States

event = dp.any_message(state=States.broadcast)
text = 'Начинаю рассылку..'
