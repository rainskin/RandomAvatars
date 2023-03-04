from assets import PictureCategory
from core import *
from .. import assets as start


class PictureMenu(ReplyKeyboard):
    get_another = '♻️ Ещё'
    main_menu = '🔙 Меню'

    def __init__(self):
        self.add_row(
            self.get_another,
            self.main_menu,
        )


text = """
👇 Воспользуйся меню под полем для ввода, чтобы вернуться в меню или получить другую картинку!
"""

picture_menu = PictureMenu()

BUTTON_TO_CATEGORY = [
    (start.Keyboard.anime_avatars, PictureCategory.AVATAR),
    (start.Keyboard.paired_avatars, PictureCategory.PAIRED_AVATARS),
    (start.Keyboard.cute_pictures, PictureCategory.CUTE),
    (start.Keyboard.angry_pictures, PictureCategory.ANGRY),
]

event = dp.click([i[0] for i in BUTTON_TO_CATEGORY])
