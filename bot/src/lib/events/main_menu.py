from assets import kbs
from core import dp

_PICTURE_BUTTONS = [
    kbs.MainMenu.anime_avatars,
    kbs.MainMenu.paired_avatars,
    kbs.MainMenu.cute_pictures,
    kbs.MainMenu.angry_pictures,
]

get_picture = dp.click(_PICTURE_BUTTONS)
