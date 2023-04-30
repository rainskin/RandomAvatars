from botty import bot, Message, User, Answer, is_private, bold

from api import Text
from assets import kbs


def menu(user: User):
    text = Text.GREET.format(mention=user.get_mention())
    return Answer(text, kbs.Menu(bot.startgroup_url))


def start(msg: Message):
    if is_private(msg.chat):
        return menu(msg.from_user)
    return GREET_GROUP


def utm(key_count: dict[str, int]):
    strings = [f"{bold(k)}: {c}" for k, c in key_count.items()]
    return Answer("\n".join(strings), kbs.CANCEL)


def wait_for(seconds: int):
    return Answer(Text.WAIT_FOR.format(seconds=seconds))


def join_required(url: str):
    return Answer(Text.JOIN_REQUIRED.format(url=url))


def required_join(invite_link: str | None = None):
    if invite_link:
        text = Text.REQUIRED_JOIN.format(invite_link)
    else:
        text = Text.REQUIRED_JOIN_DISABLED
    return Answer(text, kbs.RequiredJoin(not invite_link))


GREET_GROUP = Answer(Text.GREET_GROUP)
PICTURE_MENU = Answer(Text.PICTURE_MENU_HINT, kbs.PICTURE_MENU)
DOES_NOT_WORK = Answer(Text.DOES_NOT_WORK)
ADMIN_MENU = Answer(Text.ADMIN_PANEL, kbs.ADMIN_MENU)
ASK_POST = Answer(Text.ASK_POST, kbs.CANCEL)
BROADCAST_START = Answer(Text.BROADCAST_START)
REQUIRED_JOIN = required_join()
ASK_CHANNEL_POST = Answer(Text.ASK_CHANNEL_POST, kbs.CANCEL)
FORWARD_ERROR = Answer(Text.FORWARD_ERROR)
RIGHTS_ERROR = Answer(Text.RIGHTS_ERROR)
ASK_RIGHTS = Answer(Text.ASK_RIGHTS)
