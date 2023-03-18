from core import handlers
from lib.Start import Texts, Keyboard


class MenuRequest(handlers.Text):

    async def prepare(self):
        if self.is_chat_private:
            self.reply_text = Texts.for_private_chat.format(self.user_mention)
            self.reply_keyboard = Keyboard(self.startgroup_url)
        else:
            self.reply_text = Texts.for_group
