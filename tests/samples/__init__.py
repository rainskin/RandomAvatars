from aiogram import Bot
from botty import User, bot

from deps import mention

NAME = "Dmitriy"
ID = 724477101
USERNAME = "test7244bot"
STARTGROUP_URL = f"https://t.me/{USERNAME}?startgroup=0"
MENTION = mention(NAME, ID)
USER = User(id=ID, first_name=NAME)
ME = User(username=USERNAME)
REQUIRED_JOIN_URL = "https://t.me/+HDP373UDT-4wMTVi"

Bot.set_current(bot)
bot._me = ME  # noqa: SLF001 #type: ignore
