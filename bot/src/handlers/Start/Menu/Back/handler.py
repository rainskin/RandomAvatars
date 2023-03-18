from core import TextHandler
from lib import MenuRequestHandler, Menu


class Back(TextHandler, MenuRequestHandler):
    trigger = Menu.Keyboard.BACK
