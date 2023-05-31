from typing import TYPE_CHECKING

from botty import Message, User, bold, bot, is_private

from deps import Answer

from . import kbs as k
from . import texts as t

if TYPE_CHECKING:
    from api import Sign


greet_group = Answer(t.greet_group)
picture_menu = Answer(t.picture_menu_hint, k.picture_menu)
does_not_work = Answer(t.does_not_work)
admin_menu = Answer(t.admin_panel, k.admin_menu)
ask_post = Answer(t.ask_post, k.cancel)
broadcast_start = Answer(t.broadcast_start)
ask_channel_post = Answer(t.ask_channel_post, k.cancel)
forward_error = Answer(t.forward_error)
rights_error = Answer(t.rights_error)
ask_rights = Answer(t.ask_rights)
signs = Answer(t.admin_panel, k.signs)
ask_sign = Answer(t.ask_sign, k.cancel)
only_for_groups = Answer(t.only_for_groups)
ask_picture_recipient = Answer(t.ask_picture_recipient)
select_picture = Answer(t.select_picture, k.select_picture())


def picture_sent(url: str):
    return Answer(t.picture_sent(url))


def start(msg: Message):
    if is_private(msg.chat):
        return menu(msg.from_user)
    return greet_group


def utm(key_count: dict[str, int]):
    strings = [f"{bold(k)}: {c}" for k, c in key_count.items()]
    return Answer("\n".join(strings), k.cancel)


def wait_for(seconds: int):
    return Answer(t.wait_for(seconds))


def join_required(links: list[str]):
    return Answer(t.join_required, k.join_required(links))


def sign(s: "Sign"):
    return Answer(s.text, k.sign_menu(s.str_id))


def menu(user: User):
    text = t.greet(user.get_mention())
    return Answer(text, k.menu(bot.startgroup_url))


def send_picture_info(group_id: int):
    kb = k.start_from_group(group_id)
    return Answer(t.send_picture_info, kb)


def required_join_chat(chat_id: int, invite_link: str):
    return Answer(invite_link, k.delete_required_join(chat_id))


required_join = Answer(t.admin_panel, k.required_join)


def reselect_picture(picture: str):
    return Answer(t.select_another_picture, k.select_picture(with_send=True), picture)
