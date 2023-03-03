from core.keyboards import InlineKeyboard, CallbackButton

BACK_BUTTON = CallbackButton('🔙 Назад')


class MainKeyboard(InlineKeyboard):
    broadcast = CallbackButton('📩 Рассылка')
    required_join = CallbackButton('✅ Обязательная подписка')

    def __init__(self):
        self.add_rows(
            self.broadcast,
            self.required_join,
        )


class CancelKeyboard(InlineKeyboard):

    def __init__(self):
        self.add_row(BACK_BUTTON)


main_keyboard = MainKeyboard()
cancel_keyboard = CancelKeyboard()

menu_text = 'Вот твоя админ-панель, хозяин 🥵'
