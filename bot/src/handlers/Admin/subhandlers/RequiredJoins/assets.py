from core import dp
from core.keyboards import InlineKeyboard, CallbackButton
from ... import assets as admin


class Keyboard(InlineKeyboard):
    select_channel = CallbackButton('Выбрать канал')
    disable = CallbackButton('Отключить')

    def __init__(self):
        self.add_rows(
            self.select_channel,
            self.disable,
            admin.BACK_BUTTON,
        )


keyboard = Keyboard()
event = dp.click(admin.main_keyboard.required_join)
