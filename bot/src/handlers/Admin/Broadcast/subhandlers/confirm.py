import lib
from core import QueryHandler
from lib.Confirm import text


class Confirm(QueryHandler):
    trigger = lib.Post.Keyboard.CONFIRM
    reply_text = text
    next_state = None

    async def prepare(self):
        print('Запускаю рассылку')  # TODO
