from . import Admin, Errors, GetCommands, SendPicture, TextMessage


def setup():
    # Start.setup()
    Admin.setup()
    GetCommands.setup()
    SendPicture.setup()
    TextMessage.setup()
    Errors.setup()
