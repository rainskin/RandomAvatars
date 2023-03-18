from core import Handlers
from . import Menu
from .handler import Start

HANDLERS = Handlers(
    Start,
    Menu.HANDLERS,
)
