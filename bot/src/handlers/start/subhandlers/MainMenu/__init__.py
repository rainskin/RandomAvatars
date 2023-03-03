from . import subhandlers
from .assets import event
from .controller import Controller

Controller.setup_on(event)
subhandlers.setup()
