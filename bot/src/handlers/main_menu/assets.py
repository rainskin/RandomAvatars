from core import dp

from assets.keyboards import MainMenu

_PICTURE_BUTTONS = [
    MainMenu.anime_avatars,
    MainMenu.paired_avatars,
    MainMenu.cute_pictures,
    MainMenu.angry_pictures,
]

event = dp.click(_PICTURE_BUTTONS)
