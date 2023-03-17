from core import keyboards


class Keyboard(keyboards.Reply):
    GET_ANOTHER = '♻️ Ещё'
    BACK = '🔙 Меню'

    buttons = [GET_ANOTHER, BACK]
    row_width = 2


class Texts:
    menu_hint = """
👇 Воспользуйся меню под полем для ввода, чтобы вернуться в меню или получить другую картинку!
"""
    wait = 'Прежде, чем выполнить эту команду подожди {} сек.'
    required_join = 'Чтобы пользоваться ботом здесь, тебе необходимо подписаться на наш канал: {}'
