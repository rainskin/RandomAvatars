from botty import ReplyMarkup

import assets.kbs as k

from .samples import STARTGROUP_URL
from .samples import kbs as s


def check(kb: ReplyMarkup, as_dict: dict):  # type: ignore[reportMissingTypeArgument]
    assert kb.to_python() == as_dict


def check_all(*names: str):
    for name in names:
        check(getattr(k, name), getattr(s, name))


def test():
    check(k.menu(STARTGROUP_URL), s.menu)
    check(k.sign_menu("0"), s.sign_menu)
    check(k.required_join(), s.required_join)
    check(k.required_join(disabled=True), s.required_join_disabled)
    check(k.start_from_group(0), s.start_from_group)
    check_all(
        "picture_menu",
        "admin_menu",
        "signs",
        "cancel",
        "select_picture",
    )
