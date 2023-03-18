from core import Handlers
from . import GetAnother, Back
from .handler import MainMenu

HANDLERS = Handlers(
    MainMenu,
    GetAnother.HANDLERS,
    Back.HANDLERS,
)
