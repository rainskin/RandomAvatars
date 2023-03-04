from core import dp
from ... import assets as broadcast

event = dp.any_message(state=broadcast.state)
text = 'Начинаю рассылку..'
