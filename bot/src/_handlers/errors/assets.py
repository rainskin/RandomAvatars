from aiogram.utils.exceptions import BadRequest
from core import dp

no_send_photo_rights_text = """
Похоже, у меня нет прав для отправки картинок в этот чат.
Пожалуйста, проверьте мои/общие права в настройках группы или дайте мне права администратора.
"""

event = dp.errors_handler(exception=BadRequest)
