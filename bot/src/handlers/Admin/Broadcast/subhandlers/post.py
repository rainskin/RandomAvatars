from core import TextHandler
from lib.Broadcast import states
from lib.Post import text, Keyboard


class Post(TextHandler):
    reply_text = text
    reply_keyboard = Keyboard
    next_state = states.CONFIRM

    async def prepare(self):
        self.context.chat_data['post_id'] = self.message_id
        await self.copy()
