from core import keyboards
from lib.assets import PictureCategory, MenuKeyboard


class Keyboard(keyboards.Reply):
    GET_ANOTHER = '♻️ Ещё'
    BACK = '🔙 Меню'

    buttons = [GET_ANOTHER, BACK]
    row_width = 2


text = '👇 Воспользуйся меню под полем для ввода, чтобы вернуться в меню или получить другую картинку!'

CATEGORY_BY_TRIGGER = {
    MenuKeyboard.ANIME_AVATARS: PictureCategory.AVATAR,
    MenuKeyboard.PAIRED_AVATARS: PictureCategory.PAIRED_AVATARS,
    MenuKeyboard.CUTE_PICTURES: PictureCategory.CUTE,
    MenuKeyboard.ANGRY_PICTURES: PictureCategory.ANGRY,
}
