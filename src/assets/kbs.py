# from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, \
#     ReplyKeyboardMarkup

from core.keyboards import InlineKeyboard, CallbackButton, UrlButton


# # Раздел загрузки контента
# upload_btn = InlineKeyboardButton('Загрузить контент', callback_data='upload')
# admin = InlineKeyboardMarkup().add(upload_btn)
#
# # Категории
# single_avatars_btn = InlineKeyboardButton('Обычные авы', callback_data='single_avatars')
# paired_avatars_btn = InlineKeyboardButton('Парные авы', callback_data='paired_avatars')
#
# # Клавиатура категорий
# content_category_kb = InlineKeyboardMarkup(row_width=1).add(single_avatars_btn, paired_avatars_btn)
#
# # Кнопка 'Готово'
# done_btn = KeyboardButton('Готово')
# done_kb = ReplyKeyboardMarkup(resize_keyboard=True).add(done_btn)
#
# # Удалить клавиатуру
# remove = ReplyKeyboardRemove()


class MainMenu(InlineKeyboard):
    add_to_chat = UrlButton('💬 Добавить в чат', '{startgroup_url}')
    anime_avatars = CallbackButton('⛩ Аниме авы')
    paired_avatars = CallbackButton('🎎 Парные аватарки')
    cute_pictures = CallbackButton('💖 Милые пикчи')
    angry_pictures = CallbackButton('😡 Агрессивные')

    def __init__(self, startgroup_url: str):
        self.add_row(
            self.add_to_chat.format(startgroup_url=startgroup_url),
        )
        self.add_rows(
            self.anime_avatars,
            self.paired_avatars,
            self.cute_pictures,
            self.angry_pictures,
            width=2,
        )
