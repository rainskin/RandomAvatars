from core import Handlers
from . import Start, GetCommands, Text, SendPicture, Admin

HANDLERS = Handlers(
    Start.HANDLERS,
    GetCommands.HANDLERS,
    SendPicture.HANDLERS,
    Admin.HANDLERS,
    Text.HANDLERS,
)
