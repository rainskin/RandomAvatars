import config
from assets import PictureCategory, commands
from assets import keyboards
from core import *


class PictureCategoryPicker:

    def __init__(self, event: EVENT):
        self._event = event

    def pick(self) -> PictureCategory | None:
        if isinstance(self._event, MESSAGE):
            return self._pick_from_message()
        return self._pick_from_query()

    def _pick_from_message(self) -> PictureCategory | None:
        if command := self._event.get_command(pure=True):
            words = [command]
        else:
            words = self._event.text.lower().split()

        triggers_to_category = [
            (config.TriggerWords.AVATAR + [commands.GET_AVATARS], PictureCategory.AVATAR),
            (config.TriggerWords.PAIRED_AVATARS + [commands.GET_PAIRED], PictureCategory.PAIRED_AVATARS),
            (config.TriggerWords.CUTE_PICTURE + [commands.GET_CUTE], PictureCategory.CUTE),
            (config.TriggerWords.ANGRY_PICTURE + [commands.GET_ANGRY], PictureCategory.ANGRY),
        ]

        for word in words:
            for triggers, category in triggers_to_category:
                if word in triggers:
                    return category

    def _pick_from_query(self) -> PictureCategory | None:
        kb = keyboards.MainMenu

        button_to_category = [
            (kb.anime_avatars, PictureCategory.AVATAR),
            (kb.paired_avatars, PictureCategory.PAIRED_AVATARS),
            (kb.cute_pictures, PictureCategory.CUTE),
            (kb.angry_pictures, PictureCategory.ANGRY),
        ]

        for button, category in button_to_category:
            if self._event.data == button.data:
                return category
