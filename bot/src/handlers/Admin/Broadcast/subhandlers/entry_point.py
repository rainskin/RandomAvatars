import lib
from core import QueryHandler
from lib.Broadcast import states, text


class EntryPoint(QueryHandler):
    trigger = lib.Admin.MenuKeyboard.BROADCAST
    edit_text = text
    edit_keyboard = lib.Admin.CancelKeyboard
    next_state = states.POST
