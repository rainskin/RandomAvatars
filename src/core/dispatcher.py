import aiogram
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from .bot import Bot, bot
from .keyboards import CallbackButton


class Dispatcher(aiogram.Dispatcher):
    def __init__(self, _bot: Bot):
        super().__init__(_bot, storage=MemoryStorage())

    def command(self, value: str):
        return self.message_handler(commands=value)

    def click(self, button: CallbackButton):
        return self.callback_query_handler(text=button.data)


dp = Dispatcher(bot)
