from aiogram.types import BotCommand

START = 'start'
GET_AVATARS = 'get_avatars'
GET_PAIRED = 'get_paired'
GET_CUTE = 'get_cute'
GET_ANGRY = 'get_angry'
SEND_PICTURE = 'send_picture'
ADMIN = 'admin'


class Groups:
    USER = [
        BotCommand(START, 'Главное меню'),
        BotCommand(GET_AVATARS, 'Получить аватарку'),
        BotCommand(GET_PAIRED, 'Получить парные аватарки'),
        BotCommand(GET_CUTE, 'Получить милую пикчу'),
        BotCommand(GET_ANGRY, 'Получить агрессивную пикчу'),
        BotCommand(SEND_PICTURE, 'Отправить пикчу пользователю'),
    ]

    ADMIN = USER + [
        BotCommand(ADMIN, 'Админ-панель'),
    ]
