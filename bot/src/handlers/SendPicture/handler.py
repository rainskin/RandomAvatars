from core import CommandHandler
from lib import commands


class SendPicture(CommandHandler):
    trigger = commands.SEND_PICTURE
    reply_text = '🙃 Команда временно не работает. Скоро починим!'
