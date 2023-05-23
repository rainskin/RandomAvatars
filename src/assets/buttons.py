from botty import CallbackButton, UrlButton, bot

DELETE_SIGN = CallbackButton("Удалить", "delete-sign:{id}")
GROUP_PREFIX = "group"

back = CallbackButton("🔙 Назад")
anime_avatars = CallbackButton("⛩ Аниме авы")
paired_avatars = CallbackButton("🎎 Парные аватарки")
cute_pictures = CallbackButton("💖 Милые пикчи")
angry_pictures = CallbackButton("😡 Агрессивные")
get_another = "♻️ Ещё"
menu = "🔙 Меню"
broadcast = CallbackButton("📩 Рассылка")
required_join = CallbackButton("✅ Обязательная подписка")
utm = CallbackButton("🏷 UTM (Рефералы)")
signs = CallbackButton("✍️ Подписи")
add_sign = CallbackButton("Добавить подпись")
show_signs = CallbackButton("Просмотреть подписи")
select_channel = CallbackButton("Выбрать канал")
disable = CallbackButton("Отключить")


def start_from_group(group_id: int):
    url = bot.get_start_url(f"{GROUP_PREFIX}{group_id}")
    return UrlButton("Продолжить", url)


def delete_sign(sign_id: str):
    return DELETE_SIGN.format(id=sign_id)


def add_to_chat(startgroup_url: str):
    return UrlButton("💬 Добавить в чат", startgroup_url)


send = CallbackButton("▶️ Отправить")
