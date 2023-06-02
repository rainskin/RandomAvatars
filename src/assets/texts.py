from deps.texts import t

from .types import Command


def greet(mention: str):
    return t.get("greet", mention=mention)


def wait_for(seconds: int):
    return t.get("wait-for", seconds=seconds)


join_required = t.get("join-required")


def required_join(url: str | None = None):
    return t.get("required-join", url=url or disabled)


def picture_for(recipient: str, from_user: str):
    return t.get("picture-for", recipient=recipient, from_user=from_user)


def picture_sent(url: str):
    return t.get("picture-sent", url=url)


def _greet_group(**commands: Command):
    return t.get("greet-group", **commands)


greet_group = _greet_group(
    cmd1="get_avatars",
    cmd2="get_paired",
    cmd3="get_cute",
    cmd4="get_angry",
    cmd5="send_picture",
)

only_for_groups = t.get("only-for-groups")
send_picture_info = t.get("send-picture-info")
ask_picture_recipient = t.get("ask-picture-recipient")
select_picture = t.get("select-picture")
picture_menu_hint = t.get("picture-menu-hint")
does_not_work = t.get("does-not-work")
ask_rights = t.get("ask-rights")
admin_panel = t.get("admin-panel")
ask_post = t.get("ask-post")
broadcast_start = t.get("broadcast-start")
disabled = t.get("disabled")
required_join_disabled = required_join()
ask_channel_post = t.get("ask-channel-post")
forward_error = t.get("forward-error")
rights_error = t.get("rights-error")
ask_sign = t.get("ask-sign")
no_signs = t.get("no-signs")
no_required_join = t.get("no-required-join")
select_another_picture = t.get("select-another-picture")
required_join_checked = t.get("required-join-checked")
required_join_check_failed = t.get("required-join-check-failed")
