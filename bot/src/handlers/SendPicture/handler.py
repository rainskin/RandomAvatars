from core import handlers
from lib import commands


class SendPicture(handlers.Command):
    trigger = commands.SEND_PICTURE
    reply_text = '🙃 Команда временно не работает. Скоро починим!'
