from core import Handlers
from . import Start, GetCommands, Text, SendPicture

HANDLERS = Handlers(
    Start.HANDLERS,
    GetCommands.HANDLERS,
    SendPicture.HANDLERS,
    Text.HANDLERS,
)
