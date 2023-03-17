import os

ADMIN_IDS = [724477101, 936845322]
API_BASE_URL = os.environ['API_BASE_URL']


class TriggerWords:  # lowercase!
    avatar = ['аватарка', 'аватарку', 'ава', 'аву']
    paired_avatars = ['авы', 'парные', 'аватарки']
    cute_picture = ['милую']
    angry_picture = ['злую', 'агресивную', 'агрессивную']


SIGNS = [
    '{mention}, вот твоя аватарка!',
    '{mention}, держи!',
    '{mention}, лови! Подобрали специально для тебя',
]
