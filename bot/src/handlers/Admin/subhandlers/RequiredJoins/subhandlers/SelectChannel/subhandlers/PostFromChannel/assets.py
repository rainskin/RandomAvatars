from core import dp

from ... import assets as select_channel

event = dp.any_message(state=select_channel.state)
forward_error_text = 'Ошибка, не вижу источник пересылки'
rights_error_text = 'У меня нет нужных прав в этом канале'
success_text = 'Обязательная подписка настроена'
