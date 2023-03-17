from core import keyboards


class Keyboard(keyboards.Reply):
    GET_ANOTHER = '♻️ Ещё'
    BACK = '🔙 Меню'

    buttons = [GET_ANOTHER, BACK]
    row_width = 2


text = '👇 Воспользуйся меню под полем для ввода, чтобы вернуться в меню или получить другую картинку!'
