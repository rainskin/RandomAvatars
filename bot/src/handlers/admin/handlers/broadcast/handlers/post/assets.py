from core import dp
from assets import STATES

event = dp.any_message(state=STATES.broadcast)
text = 'Начинаю рассылку..'
