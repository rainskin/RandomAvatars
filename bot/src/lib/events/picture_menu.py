from lib.assets import kbs
from core import dp

get_another = dp.click(kbs.PictureMenu.get_another)
old_get_another = dp.text('♻️ Хочу другую')
main_menu = dp.click(kbs.PictureMenu.main_menu)
