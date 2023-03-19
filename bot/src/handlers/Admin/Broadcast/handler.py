from core import ConversationHandler
from lib.Admin import CancelHandler
from lib.Broadcast import states
from . import subhandlers


class Broadcast(ConversationHandler):
    entry_point = subhandlers.EntryPoint
    subhandlers = {
        states.POST: subhandlers.Post,
        states.CONFIRM: subhandlers.Confirm,
    }
    fallback = CancelHandler
