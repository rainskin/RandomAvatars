from . import Disable, SelectChannel
from .assets import event
from .controller import Controller


def setup():
    Controller.setup_on(event)
    Disable.setup()
    SelectChannel.setup()
