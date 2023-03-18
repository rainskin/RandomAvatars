from aiogram.utils.exceptions import BadRequest

from core import dp


class Texts:
    no_send_photo_rights = """
Похоже, у меня нет прав для отправки картинок в этот чат.
Пожалуйста, проверьте мои/общие права в настройках группы или дайте мне права администратора.
"""


event = dp.errors_handler(exception=BadRequest)


class ErrorDescriptions:
    no_send_photo_rights = 'Not enough rights to send photos to the chat'
    no_send_text_rights = 'Not enough rights to send text messages to the chat'
