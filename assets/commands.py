from botty import BotCommand

from api import Command


class Groups:
    FOR_USERS = [
        BotCommand(Command.START, "Главное меню"),
        BotCommand(Command.GET_AVATARS, "Получить аватарку"),
        BotCommand(Command.GET_PAIRED, "Получить парные аватарки"),
        BotCommand(Command.GET_CUTE, "Получить милую пикчу"),
        BotCommand(Command.GET_ANGRY, "Получить агрессивную пикчу"),
        BotCommand(Command.SEND_PICTURE, "Отправить пикчу пользователю"),
    ]
    FOR_ADMINS = FOR_USERS + [
        BotCommand(Command.ADMIN, "Админ-панель"),
    ]
