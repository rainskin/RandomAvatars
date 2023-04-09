from . import Broadcast, RequiredJoins, Cancel, Utm
from .assets import event
from .controller import Controller


def setup():
    Controller.setup_on(event)
    Broadcast.setup()
    RequiredJoins.setup()
    Utm.setup()
    Cancel.setup()
