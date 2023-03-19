from core import InlineKeyboard
from lib.Admin import BACK_BUTTON


class Keyboard(InlineKeyboard):
    CONFIRM = 'Запускай!'
    buttons = [CONFIRM, BACK_BUTTON]


text = 'Начать рассылку?'
