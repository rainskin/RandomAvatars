from . import GetAnother, MainMenu
from .assets import event
from .controller import Controller


def setup():
    Controller.setup_on(event)
    GetAnother.setup()
    MainMenu.setup()
