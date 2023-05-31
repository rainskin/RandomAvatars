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


required_join = ik(b.add_channel, b.show_channels, b.back)


def start_from_group(group_id: int):
    return ik(b.start_from_group(group_id))


def select_picture(*, with_send: bool = False):
    kb = ik(b.cute_pictures, b.angry_pictures, row_width=2)
    if with_send:
        kb.add(b.send)
    return kb


def delete_required_join(chat_id: int):
    return ik(b.delete_required_join(chat_id))


def join_required(links: list[str]):
    buttons = [b.required_join_link(index+1, link) for index, link in enumerate(links)]
    return ik(*buttons)


picture_menu = rk(b.get_another, b.menu, row_width=2)
admin_menu = ik(b.broadcast, b.required_join, b.utm, b.signs)
signs = ik(b.add_sign, b.show_signs, b.back)
cancel = ik(b.back)
