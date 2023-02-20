from core.keyboards import InlineKeyboard, CallbackButton, UrlButton, ReplyKeyboard, RemovedKeyboard


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


removed = RemovedKeyboard().create()


class AdminPanel(InlineKeyboard):
    broadcast = CallbackButton('📩 Рассылка')

    def __init__(self):
        self.add_row(self.broadcast)


admin_panel = AdminPanel().create()


class Cancel(InlineKeyboard):
    button = CallbackButton('Отменить')

    def __init__(self):
        self.add_row(self.button)


cancel = Cancel().create()
