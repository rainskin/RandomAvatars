import config
from . import events, answers
from .assets import PictureCategory, commands, kbs
from .broadcast import Broadcast
from .consts import *
from .loader import api
from .picture_request import PictureRequest
from .utils import get_chat_invite_link, reset_state


def on_picture_request(request: REQUEST, category: PictureCategory):
    return PictureRequest(request, category).respond()


def is_admin(user: USER) -> bool:
    return user.id in config.ADMIN_IDS


def contain_trigger_words(text: str, trigger_words: list[str]) -> bool:
    text_words = text.split()

    for tw in trigger_words:
        if tw in text_words:
            return True

    return False


TRIGGERS_TO_CATEGORY = [
    (config.TriggerWords.AVATAR + [commands.GET_AVATARS], PictureCategory.AVATAR),
    (config.TriggerWords.PAIRED_AVATARS + [commands.GET_PAIRED], PictureCategory.PAIRED_AVATARS),
    (config.TriggerWords.CUTE_PICTURE + [commands.GET_CUTE], PictureCategory.CUTE),
    (config.TriggerWords.ANGRY_PICTURE + [commands.GET_ANGRY], PictureCategory.ANGRY),
]


def schedule_broadcast(post: MESSAGE):
    Broadcast(post).schedule()


def save_chat(chat: CHAT):
    return api.save_chat(chat.id)


def update_my_commands():
    return commands.setup()


def choose_picture_category(request: REQUEST) -> PictureCategory | None:
    if isinstance(request, MESSAGE):
        return _choose_picture_category_message(request)
    return _choose_picture_category_query(request)


def _choose_picture_category_message(request: MESSAGE) -> PictureCategory | None:
    if command := request.get_command(pure=True):
        words = [command]
    else:
        words = request.text.split()

    for word in words:
        for triggers, category in TRIGGERS_TO_CATEGORY:
            if word in triggers:
                return category


def _choose_picture_category_query(request: QUERY) -> PictureCategory | None:
    kb = kbs.MainMenu

    button_to_category = [
        (kb.anime_avatars, PictureCategory.AVATAR),
        (kb.paired_avatars, PictureCategory.PAIRED_AVATARS),
        (kb.cute_pictures, PictureCategory.CUTE),
        (kb.angry_pictures, PictureCategory.ANGRY),
    ]

    for button, category in button_to_category:
        if request.data == button.data:
            return category


async def get_picture_category(for_user: USER) -> PictureCategory | None:
    return await api.get_picture_category(for_user.id)


def reset_required_join():
    return api.required_join.set_chat_id(None)
