from enum import StrEnum


class PictureCategory(StrEnum):
    AVATAR = 'avatar'
    PAIRED_AVATARS = 'paired_avatars'
    CUTE = 'cute'
    ANGRY = 'angry'


class Texts:
    wait = 'Прежде, чем выполнить эту команду подожди {} сек.'
    required_join = 'Чтобы пользоваться ботом здесь, тебе необходимо подписаться на наш канал: {}'
