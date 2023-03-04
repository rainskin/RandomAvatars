# from . import MainMenu
from .assets import event
from .controller import Controller


def setup():
    Controller.setup_on(event)
    # MainMenu.setup()
