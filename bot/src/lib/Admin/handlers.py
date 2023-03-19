from core import QueryHandler
from .assets import BACK_BUTTON, text, MenuKeyboard


class CancelHandler(QueryHandler):
    trigger = BACK_BUTTON
    edit_text = text
    edit_keyboard = MenuKeyboard
    next_state = None
