from core import handlers
from lib.assets import Texts, MenuKeyboard


class MenuRequestHandler(handlers.Message):

    async def prepare(self):
        if self.is_chat_private:
            self.reply_text = Texts.private_welcome.format(self.user_mention)
            self.reply_keyboard = MenuKeyboard(self.startgroup_url)
        else:
            self.reply_text = Texts.group_welcome
