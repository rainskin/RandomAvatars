from core import Handlers
from . import Broadcast
from .handler import Admin

HANDLERS = Handlers(
    Admin,
    Broadcast.HANDLERS,
)
