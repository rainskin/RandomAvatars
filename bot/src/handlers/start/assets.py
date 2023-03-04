from assets import commands
from core import *
from core.keyboards import *

event = dp.command(commands.START, state='*')

welcome_text = """
⛩ Привет, {mention}!

Я буду отправлять тебе аватарки и классные пикчи, которые ты сможешь использовать в своих диалогах 👌🏻

Добавляй меня в свой чат или начинай пользоваться прямо здесь 😉
"""

group_welcome_text = f"""
💕 Спасибо, что добавили меня!

Я умею отправлять аватарки и пикчи для диалогов. Попробуй одну из этих команд:

👉🏻 /{commands.GET_AVATARS} 👉🏻 /{commands.GET_PAIRED}
👉🏻 /{commands.GET_CUTE} 👉🏻 /{commands.GET_ANGRY}
👉🏻 /{commands.SEND_PICTURE}
"""


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
