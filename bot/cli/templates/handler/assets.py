from core import *
from core.keyboards import ReplyKeyboard


class Keyboard(ReplyKeyboard):
    button1 = 'Button1'
    button2 = 'Button2'

    def __init__(self):
        self.add_rows(
            self.button1,
            self.button2,
        )


event = dp.text()
next_state = State(__name__)
text = 'Hello, world!'
keyboard = Keyboard()
