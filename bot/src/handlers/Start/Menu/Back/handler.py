from core import TextHandler
from lib import MenuRequestHandler, Menu


class Back(MenuRequestHandler, TextHandler):
    trigger = Menu.Keyboard.BACK
