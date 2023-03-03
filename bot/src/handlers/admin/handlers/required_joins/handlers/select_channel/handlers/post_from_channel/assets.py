from core import dp

from lib import STATES

event = dp.any_message(state=STATES.required_join)
forward_error_text = 'Ошибка, не вижу источник пересылки'
rights_error_text = 'У меня нет нужных прав в этом канале'
success_text = 'Обязательная подписка настроена'
