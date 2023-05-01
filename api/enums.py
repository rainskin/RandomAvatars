from enum import StrEnum

from i_texts import texts as t


class PictureCategory(StrEnum):
    AVATAR = "avatar"
    PAIRED_AVATARS = "paired_avatars"
    CUTE = "cute"
    ANGRY = "angry"


class ChatType(StrEnum):
    PRIVATE = "private"
    GROUP = "group"
    SUPERGROUP = "supergroup"


class Command:
    START = "start"
    GET_AVATARS = "get_avatars"
    GET_PAIRED = "get_paired"
    GET_CUTE = "get_cute"
    GET_ANGRY = "get_angry"
    SEND_PICTURE = "send_picture"
    ADMIN = "admin"


class Text:
    GREET = t["greet"]
    GREET_GROUP = t["greetGroup"].format(
        Command.GET_AVATARS,
        Command.GET_PAIRED,
        Command.GET_CUTE,
        Command.GET_ANGRY,
        Command.SEND_PICTURE,
    )
    PICTURE_MENU_HINT = t["pictureMenuHint"]
    DOES_NOT_WORK = t["doesNotWork"]
    WAIT_FOR = t["waitFor"]
    JOIN_REQUIRED = t["joinRequired"]
    ASK_RIGHTS = t["askRights"]
    ADMIN_PANEL = t["adminPanel"]
    ASK_POST = t["askPost"]
    BROADCAST_START = t["broadcastStart"]
    REQUIRED_JOIN = t["requiredJoin"]
    DISABLED = t["disabled"]
    REQUIRED_JOIN_DISABLED = REQUIRED_JOIN.format(DISABLED)
    ASK_CHANNEL_POST = t["askChannelPost"]
    FORWARD_ERROR = t["forwardError"]
    RIGHTS_ERROR = t["rightsError"]
    ASK_SIGN = "Отправь подпись"
    NO_SIGNS = "Нет подписей"
