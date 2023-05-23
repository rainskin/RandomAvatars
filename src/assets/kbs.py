from deps import inline_keyboard as ik
from deps import reply_keyboard as rk

from . import buttons as b

PICTURE_BUTTONS = [b.anime_avatars, b.paired_avatars, b.cute_pictures, b.angry_pictures]


def menu(startgroup_url: str):
    return ik(*PICTURE_BUTTONS, row_width=2).add(
        b.add_to_chat(startgroup_url),
    )


def sign_menu(sign_id: str):
    return ik(b.delete_sign(sign_id))


def required_join(*, disabled: bool = False):
    buttons = [b.select_channel, b.back]
    if not disabled:
        buttons.insert(1, b.disable)
    return ik(*buttons)


def start_from_group(group_id: int):
    return ik(b.start_from_group(group_id))


def select_picture(*, with_send: bool = False):
    kb = ik(b.cute_pictures, b.angry_pictures, row_width=2)
    if with_send:
        kb.add(b.send)
    return kb


picture_menu = rk(b.get_another, b.menu, row_width=2)
admin_menu = ik(b.broadcast, b.required_join, b.utm, b.signs)
signs = ik(b.add_sign, b.show_signs, b.back)
cancel = ik(b.back)
