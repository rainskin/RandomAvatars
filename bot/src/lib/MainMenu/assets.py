from core import keyboards
from lib.assets import PictureCategory
from .. import Start


class Keyboard(keyboards.Reply):
    GET_ANOTHER = '♻️ Ещё'
    BACK = '🔙 Меню'

    buttons = [GET_ANOTHER, BACK]
    row_width = 2


text = '👇 Воспользуйся меню под полем для ввода, чтобы вернуться в меню или получить другую картинку!'

CATEGORY_BY_TRIGGER = {
    Start.Keyboard.ANIME_AVATARS: PictureCategory.AVATAR,
    Start.Keyboard.PAIRED_AVATARS: PictureCategory.PAIRED_AVATARS,
    Start.Keyboard.CUTE_PICTURES: PictureCategory.CUTE,
    Start.Keyboard.ANGRY_PICTURES: PictureCategory.ANGRY,
}
