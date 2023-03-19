from lib.Admin import assets as admin


class Keyboard(InlineKeyboard):
    select_channel = CallbackButton('Выбрать канал')
    disable = CallbackButton('Отключить')

    def __init__(self):
        self.add_rows(
            self.select_channel,
            self.disable,
            admin.BACK_BUTTON,
        )


class Texts:
    info = 'Обязательная подписка: {}'
    disabled = 'Обязательная подписка отключена'


keyboard = Keyboard()
event = dp.click(admin.MenuKeyboard.required_join)
