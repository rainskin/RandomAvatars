import aiogram
from . import config


class Bot(aiogram.Bot):
    def __init__(self, token: str):
        super().__init__(token, parse_mode='html')


bot = Bot(config.BOT_TOKEN)
