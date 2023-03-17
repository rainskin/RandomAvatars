from core import dp

from .. import assets as required_joins

event = dp.click(required_joins.keyboard.disable)
text = 'Обязательная подписка отключена'
