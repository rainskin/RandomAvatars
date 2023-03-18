from core import InlineKeyboard

BACK_BUTTON = '🔙 Назад'


class MenuKeyboard(InlineKeyboard):
    BROADCAST = '📩 Рассылка'
    REQUIRED_JOIN = '✅ Обязательная подписка'

    buttons = [BROADCAST, REQUIRED_JOIN]


class CancelKeyboard(InlineKeyboard):
    buttons = [BACK_BUTTON]


text = 'Вот твоя админ-панель, хозяин 🥵'
