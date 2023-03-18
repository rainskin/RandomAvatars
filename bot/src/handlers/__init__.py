from core import Handlers
from . import Start, GetCommands, Text

HANDLERS = Handlers(
    Start.HANDLERS,
    GetCommands.HANDLERS,
    Text.HANDLERS,
)
