from core import Handlers
from . import MainMenu
from .handler import Start

HANDLERS = Handlers(
    Start,
    MainMenu.HANDLERS,
)
