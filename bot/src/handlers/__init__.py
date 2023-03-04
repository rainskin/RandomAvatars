def setup():
    from . import Admin, Errors, GetCommands, SendPicture, Start, TextMessage

    Start.setup()
    Admin.setup()
    GetCommands.setup()
    SendPicture.setup()
    TextMessage.setup()
    Errors.setup()
