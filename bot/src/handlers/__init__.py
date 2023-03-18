from core import Handlers
from . import Start, GetCommands

HANDLERS = Handlers(
    Start.HANDLERS,
    GetCommands.HANDLERS,
)
