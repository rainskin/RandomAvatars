from . import _Start, Admin, Errors, GetCommands, SendPicture, TextMessage


def setup():
    _Start.setup()
    Admin.setup()
    GetCommands.setup()
    SendPicture.setup()
    TextMessage.setup()
    Errors.setup()
