from botty import CallbackButton, NoSendPhotoRights, dp

from assets import (
    ADMIN_IDS,
    BroadcastState,
    Command,
    RequiredJoinState,
    SendPictureState,
    SignState,
)
from assets import buttons as b
from deps import on_start


def on_command(cmd: Command):
    return dp.command(cmd)


start = on_start()
send_photo_error = dp.error(NoSendPhotoRights)  # type: ignore[TODO]
text = dp.text()
admin = on_command("admin").user_id(ADMIN_IDS)
utm = dp.button(b.utm)
back = dp.button(b.back).state()


class GetCommands:
    avatar = on_command("get_avatars")
    paired = on_command("get_paired")
    cute = on_command("get_cute")
    angry = on_command("get_angry")


class Menu:
    avatar = dp.button(b.anime_avatars)
    paired = dp.button(b.paired_avatars)
    cute = dp.button(b.cute_pictures)
    angry = dp.button(b.angry_pictures)
    menu = dp.text(b.menu)
    get_another = dp.text(b.get_another)


class SendPicture:
    @staticmethod
    def on_select(button: CallbackButton):
        return dp.button(button).state(SendPictureState.picture)

    command = on_command("send_picture")
    start = on_start(b.GROUP_PREFIX)
    recipient = dp.text().state(SendPictureState.recipient)
    select_cute_picture = on_select(b.cute_pictures)
    select_angry_picture = on_select(b.angry_pictures)
    reselect_cute_picture = on_select(b.cute_pictures).state(SendPictureState.confirm)
    reselect_angry_picture = on_select(b.angry_pictures).state(SendPictureState.confirm)
    send = dp.button(b.send).state(SendPictureState.confirm)


class Signs:
    entry = dp.button(b.signs)
    show = dp.button(b.show_signs)
    delete = dp.button(b.DELETE_SIGN)
    add = dp.button(b.add_sign)
    new_text = dp.text().state(SignState.sign)


class Broadcast:
    entry = dp.button(b.broadcast)
    post = dp.message().state(BroadcastState.post)


class RequiredJoin:
    entry = dp.button(b.required_join)
    add_channel = dp.button(b.add_channel)
    channel_post = dp.message().state(RequiredJoinState.post)
    delete_channel = dp.button(b.DELETE_REQUIRED_JOIN)
    show = dp.button(b.show_channels)
    check = dp.button(b.check_join)
