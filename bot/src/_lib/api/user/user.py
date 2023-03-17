from .cooldown import Cooldown
from .picture_category import PictureCategory


class User:

    def __init__(self, base_url: str):
        self.picture_category = PictureCategory(base_url + '/picture-category')
        self.cooldown = Cooldown(base_url + '/cooldown')
