from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, \
    ReplyKeyboardMarkup

# Раздел загрузки контента
upload_btn = InlineKeyboardButton('Загрузить контент', callback_data='upload')
admin = InlineKeyboardMarkup().add(upload_btn)

# Категории
single_avatars_btn = InlineKeyboardButton('Обычные авы', callback_data='single_avatars')
paired_avatars_btn = InlineKeyboardButton('Парные авы', callback_data='paired_avatars')

# Клавиатура категорий
content_category_kb = InlineKeyboardMarkup(row_width=1).add(single_avatars_btn, paired_avatars_btn)

# Кнопка 'Готово'
done_btn = KeyboardButton('Готово')
done_kb = ReplyKeyboardMarkup(resize_keyboard=True).add(done_btn)

# Удалить клавиатуру
remove = ReplyKeyboardRemove()
