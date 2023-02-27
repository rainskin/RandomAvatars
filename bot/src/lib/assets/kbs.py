from core.keyboards import *

ADMIN_BACK_BUTTON = CallbackButton('🔙 Назад')


class MainMenu(InlineKeyboard):
    add_to_chat = UrlButton('💬 Добавить в чат', '{startgroup_url}')
    anime_avatars = CallbackButton('⛩ Аниме авы')
    paired_avatars = CallbackButton('🎎 Парные аватарки')
    cute_pictures = CallbackButton('💖 Милые пикчи')
    angry_pictures = CallbackButton('😡 Агрессивные')

    def __init__(self, startgroup_url: str):
        self.add_row(
            self.add_to_chat.format(startgroup_url=startgroup_url),
        )
        self.add_rows(
            self.anime_avatars,
            self.paired_avatars,
            self.cute_pictures,
            self.angry_pictures,
            width=2,
        )


class PictureMenu(ReplyKeyboard):
    get_another = '♻️ Ещё'
    main_menu = '🔙 Меню'

    def __init__(self):
        self.add_row(
            self.get_another,
            self.main_menu,
        )


class AdminPanel(InlineKeyboard):
    broadcast = CallbackButton('📩 Рассылка')
    required_join = CallbackButton('✅ Обязательная подписка')

    def __init__(self):
        self.add_rows(
            self.broadcast,
            self.required_join,
        )


class AdminCancel(InlineKeyboard):

    def __init__(self):
        self.add_row(ADMIN_BACK_BUTTON)


class RequiredJoin(InlineKeyboard):
    select_channel = CallbackButton('Выбрать канал')
    disable = CallbackButton('Отключить')

    def __init__(self):
        self.add_rows(
            self.select_channel,
            self.disable,
            ADMIN_BACK_BUTTON,
        )


removed = RemovedKeyboard()
admin_cancel = AdminCancel()
picture_menu = PictureMenu()
admin_panel = AdminPanel()
required_join = RequiredJoin()
