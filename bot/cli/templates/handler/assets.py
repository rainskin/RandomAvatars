from core import dp
from core.keyboards import ReplyKeyboard

from assets import STATES


class Keyboard(ReplyKeyboard):
    button1 = 'Button1'
    button2 = 'Button2'

    def __init__(self):
        self.add_rows(
            self.button1,
            self.button2,
        )


event = dp.text()
state = STATES.broadcast
text = 'Hello, world!'
keyboard = Keyboard()
