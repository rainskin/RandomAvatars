import assets.texts as t

from .samples import MENTION, REQUIRED_JOIN_URL
from .samples import texts as s


def check(text: str, sample_name: str):
    sample: str = getattr(s, sample_name)
    assert text == sample.strip()


def check_all(*names: str):
    for name in names:
        check(getattr(t, name), name)


def test():
    check(t.greet(MENTION), "greet")
    check(t.wait_for(0), "wait_for")
    check(t.join_required(REQUIRED_JOIN_URL), "join_required")
    check(t.required_join(REQUIRED_JOIN_URL), "required_join")
    check_all(
        "greet_group",
        "only_for_groups",
        "send_picture_info",
        "ask_picture_recipient",
        "select_picture",
        "picture_menu_hint",
        "does_not_work",
        "ask_rights",
        "admin_panel",
        "ask_post",
        "broadcast_start",
        "disabled",
        "required_join_disabled",
        "ask_channel_post",
        "forward_error",
        "rights_error",
        "ask_sign",
        "no_signs",
    )
