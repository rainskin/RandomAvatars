from . import Confirm
from .assets import event
from .controller import Controller


def setup():
    Controller.setup_on(event)
    Confirm.setup()
