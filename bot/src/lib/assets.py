from enum import StrEnum

from core import keyboards, buttons
from . import commands


class PictureCategory(StrEnum):
    AVATAR = 'avatar'
    PAIRED_AVATARS = 'paired_avatars'
    CUTE = 'cute'
    ANGRY = 'angry'


class Texts:
    wait = 'Прежде, чем выполнить эту команду подожди {} сек.'
    required_join = 'Чтобы пользоваться ботом здесь, тебе необходимо подписаться на наш канал: {}'
    private_welcome = """
⛩ Привет, {}!

Я буду отправлять тебе аватарки и классные пикчи, которые ты сможешь использовать в своих диалогах 👌🏻

Добавляй меня в свой чат или начинай пользоваться прямо здесь 😉
"""
    group_welcome = f"""
    💕 Спасибо, что добавили меня!

    Я умею отправлять аватарки и пикчи для диалогов. Попробуй одну из этих команд:

    👉🏻 /{commands.GET_AVATARS} 👉🏻 /{commands.GET_PAIRED}
    👉🏻 /{commands.GET_CUTE} 👉🏻 /{commands.GET_ANGRY}
    👉🏻 /{commands.SEND_PICTURE}
    """


class MenuKeyboard(keyboards.Inline):
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
