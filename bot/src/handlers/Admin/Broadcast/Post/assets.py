from core import *
from ..assets import post_state

event = dp.any_message(state=post_state)
text = 'Начинаю рассылку..'

summary_text = """
<b>Рассылка окончена</b>

Сообщений доставлено: {delivered_count} штуков
Ошибка флуда возникала: {floods_count} раз(а)
Другие ошибки: {errors_count} штуков
"""
