from core import dp

from .. import assets as select_channel

event = dp.any_message(state=select_channel.post_from_channel_state)


class Texts:
    forward_error = 'Ошибка, не вижу источник пересылки'
    rights_error = 'У меня нет нужных прав в этом канале'
    success = 'Обязательная подписка настроена'
