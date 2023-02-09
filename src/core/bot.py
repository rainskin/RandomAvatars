import aiogram

from . import config


class Bot(aiogram.Bot):
    def __init__(self, token: str):
        super().__init__(token)


bot = Bot(config.BOT_TOKEN)
