from core import *
from .. import assets as post

event = dp.click(post.Keyboard.confirm, state=post.confirm_state)
text = 'Начинаю рассылку..'

summary_text = """
<b>Рассылка окончена</b>

Сообщений доставлено: {delivered_count} штуков
Ошибка флуда возникала: {floods_count} раз(а)
Другие ошибки: {errors_count} штуков
"""
