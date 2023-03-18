import os

ADMIN_IDS = [724477101, 936845322]
API_BASE_URL = os.environ['API_BASE_URL']


class TextTriggers:  # lowercase!
    AVATAR = ['аватарка', 'аватарку', 'ава', 'аву']
    PAIRED_AVATARS = ['авы', 'парные', 'аватарки']
    CUTE_PICTURE = ['милую']
    ANGRY_PICTURE = ['злую', 'агресивную', 'агрессивную']


SIGNS = [
    '{mention}, вот твоя аватарка!',
    '{mention}, держи!',
    '{mention}, лови! Подобрали специально для тебя',
]
