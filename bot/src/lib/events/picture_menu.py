from lib.assets import kbs
from core import dp

old_get_another = dp.text('♻️ Хочу другую')
main_menu = dp.click(kbs.PictureMenu.main_menu)
