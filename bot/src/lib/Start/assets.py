from core import buttons, keyboards
from lib import commands
from lib.assets import PictureCategory


class Texts:
    for_private_chat = """
⛩ Привет, {}!

Я буду отправлять тебе аватарки и классные пикчи, которые ты сможешь использовать в своих диалогах 👌🏻

Добавляй меня в свой чат или начинай пользоваться прямо здесь 😉
"""
    for_group = f"""
💕 Спасибо, что добавили меня!

Я умею отправлять аватарки и пикчи для диалогов. Попробуй одну из этих команд:

👉🏻 /{commands.GET_AVATARS} 👉🏻 /{commands.GET_PAIRED}
👉🏻 /{commands.GET_CUTE} 👉🏻 /{commands.GET_ANGRY}
👉🏻 /{commands.SEND_PICTURE}
"""


class Keyboard(keyboards.Inline):
    ADD_TO_CHAT = buttons.Url('💬 Добавить в чат', '{}')
    ANIME_AVATARS = '⛩ Аниме авы'
    PAIRED_AVATARS = '🎎 Парные аватарки'
    CUTE_PICTURES = '💖 Милые пикчи'
    ANGRY_PICTURES = '😡 Агрессивные'

    buttons: list = [ANIME_AVATARS, PAIRED_AVATARS, CUTE_PICTURES, ANGRY_PICTURES]
    row_width = 2

    def __init__(self, startgroup_url: str):
        button = self.ADD_TO_CHAT.format(startgroup_url)
        self.buttons = self.buttons + [button]


CATEGORY_BY_BUTTON = {
    Keyboard.ANIME_AVATARS: PictureCategory.AVATAR,
    Keyboard.PAIRED_AVATARS: PictureCategory.PAIRED_AVATARS,
    Keyboard.CUTE_PICTURES: PictureCategory.CUTE,
    Keyboard.ANGRY_PICTURES: PictureCategory.ANGRY,
}
