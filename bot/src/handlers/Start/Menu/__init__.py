from core import Handlers
from . import GetAnother, Back
from .handler import Menu

HANDLERS = Handlers(
    Menu,
    GetAnother.HANDLERS,
    Back.HANDLERS,
)
