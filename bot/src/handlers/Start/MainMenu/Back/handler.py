import lib
from lib.handlers import MenuRequest


class Back(MenuRequest):
    trigger = lib.MainMenu.Keyboard.BACK
