from botty import InlineKeyboard, UrlButton, CallbackButton, ReplyKeyboard

BACK_BUTTON = CallbackButton("🔙 Назад")


class Menu(InlineKeyboard):
    ADD_TO_CHAT = UrlButton("💬 Добавить в чат", "{link}")
    ANIME_AVATARS = CallbackButton("⛩ Аниме авы")
    PAIRED_AVATARS = CallbackButton("🎎 Парные аватарки")
    CUTE_PICTURES = CallbackButton("💖 Милые пикчи")
    ANGRY_PICTURES = CallbackButton("😡 Агрессивные")

    row_width = 2
    buttons = [ANIME_AVATARS, PAIRED_AVATARS, CUTE_PICTURES, ANGRY_PICTURES]

    def __init__(self, startgroup_url: str):
        button = self.ADD_TO_CHAT.format(link=startgroup_url)
        super().__init__(button)


class PictureMenu(ReplyKeyboard):
    GET_ANOTHER = "♻️ Ещё"
    BACK = "🔙 Меню"

    buttons = [GET_ANOTHER, BACK]
    row_width = 2


class AdminMenu(InlineKeyboard):
    BROADCAST = CallbackButton("📩 Рассылка")
    REQUIRED_JOIN = CallbackButton("✅ Обязательная подписка")
    UTM = CallbackButton("🏷 UTM (Рефералы)")

    buttons = [BROADCAST, REQUIRED_JOIN, UTM]


class Cancel(InlineKeyboard):
    buttons = [BACK_BUTTON]


class RequiredJoin(InlineKeyboard):
    SELECT_CHANNEL = CallbackButton("Выбрать канал")
    DISABLE = CallbackButton("Отключить")

    buttons = [SELECT_CHANNEL]

    def __init__(self, disabled: bool):
        buttons = [] if disabled else [self.DISABLE]
        super().__init__(*buttons, BACK_BUTTON)


PICTURE_MENU = PictureMenu()
ADMIN_MENU = AdminMenu()
CANCEL = Cancel()
