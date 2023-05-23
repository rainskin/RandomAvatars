from botty import BotCommand

from .types import Command


def cmd(cmd: Command, description: str):
    return BotCommand(cmd, description)


USER_COMMANDS = [
    cmd("start", "Главное меню"),
    cmd("get_avatars", "Получить аватарку"),
    cmd("get_paired", "Получить парные аватарки"),
    cmd("get_cute", "Получить милую пикчу"),
    cmd("get_angry", "Получить агрессивную пикчу"),
    cmd("send_picture", "Отправить пикчу пользователю"),
]

ADMIN_COMMANDS = [*USER_COMMANDS, cmd("admin", "Админ-панель")]
