from telegram import BotCommand

START = 'start'
GET_AVATARS = 'get_avatars'
GET_PAIRED = 'get_paired'
GET_CUTE = 'get_cute'
GET_ANGRY = 'get_angry'
SEND_PICTURE = 'send_picture'
ADMIN = 'admin'


class Groups:
    FOR_USERS = [
        BotCommand(START, 'Главное меню'),
        BotCommand(GET_AVATARS, 'Получить аватарку'),
        BotCommand(GET_PAIRED, 'Получить парные аватарки'),
        BotCommand(GET_CUTE, 'Получить милую пикчу'),
        BotCommand(GET_ANGRY, 'Получить агрессивную пикчу'),
        BotCommand(SEND_PICTURE, 'Отправить пикчу пользователю'),
    ]

    FOR_ADMINS = FOR_USERS + [
        BotCommand(ADMIN, 'Админ-панель'),
    ]
