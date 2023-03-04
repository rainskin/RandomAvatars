from assets import PictureCategory
from core import dp
from core.keyboards import *
from ... import assets as main_menu


class PictureMenu(ReplyKeyboard):
    get_another = '♻️ Ещё'
    main_menu = '🔙 Меню'

    def __init__(self):
        self.add_row(
            self.get_another,
            self.main_menu,
        )


hint_text = """
👇 Воспользуйся меню под полем для ввода, чтобы вернуться в меню или получить другую картинку!
"""

picture_menu = PictureMenu()

BUTTON_TO_CATEGORY = [
    (main_menu.MainMenu.anime_avatars, PictureCategory.AVATAR),
    (main_menu.MainMenu.paired_avatars, PictureCategory.PAIRED_AVATARS),
    (main_menu.MainMenu.cute_pictures, PictureCategory.CUTE),
    (main_menu.MainMenu.angry_pictures, PictureCategory.ANGRY),
]

event = dp.click([i[0] for i in BUTTON_TO_CATEGORY])
