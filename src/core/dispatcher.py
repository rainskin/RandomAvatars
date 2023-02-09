import aiogram
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from .bot import Bot, bot


class Dispatcher(aiogram.Dispatcher):
    def __init__(self, _bot: Bot):
        super().__init__(_bot, storage=MemoryStorage())

    def command(self, value: str):
        return self.message_handler(commands=value)


dp = Dispatcher(bot)
