from config import ADMIN_IDS
from core import CommandHandler
from lib import commands
from lib.Admin import text, MenuKeyboard


class Admin(CommandHandler):
    trigger = commands.ADMIN
    for_users = ADMIN_IDS
    reply_text = text
    reply_keyboard = MenuKeyboard
