import config
from assets import commands
from core import *

BACK_BUTTON = CallbackButton('🔙 Назад')


class MainKeyboard(InlineKeyboard):
    broadcast = CallbackButton('📩 Рассылка')
    required_join = CallbackButton('✅ Обязательная подписка')
    utm = CallbackButton('🏷 UTM (Рефералы)')

    def __init__(self):
        self.add_rows(
            self.broadcast,
            self.required_join,
            self.utm,
        )


class CancelKeyboard(InlineKeyboard):

    def __init__(self):
        self.add_row(BACK_BUTTON)


main_keyboard = MainKeyboard()
cancel_keyboard = CancelKeyboard()
text = 'Вот твоя админ-панель, хозяин 🥵'
event = dp.command(commands.ADMIN, user_id=config.ADMIN_IDS)
