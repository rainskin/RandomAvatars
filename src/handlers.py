import callbacks
import events


def setup():
    setup_send_picture()
    events.start(callbacks.start)
    setup_get_commands()
    setup_menu()
    setup_admin()
    events.RequiredJoin.check(callbacks.required_join.check)
    events.text(callbacks.check_triggers)
    events.send_photo_error(callbacks.ask_rights)  # type: ignore[TODO]


def setup_admin():
    c = callbacks.admin
    events.admin(c.menu)
    events.back(c.back)
    events.utm(c.send_utm)
    setup_broadcast()
    setup_signs()
    setup_required_join()


def setup_get_commands():
    c = callbacks.get_command
    e = events.GetCommands
    e.avatar(c("avatar"))
    e.paired(c("paired_avatars"))
    e.cute(c("cute"))
    e.angry(c("angry"))


def setup_menu():
    c = callbacks.menu
    e = events.Menu
    e.avatar(c.send_picture("avatar"))
    e.paired(c.send_picture("paired_avatars"))
    e.cute(c.send_picture("cute"))
    e.angry(c.send_picture("angry"))
    e.menu(c.send_menu)
    e.get_another(c.send_another_picture)


def setup_broadcast():
    c = callbacks.broadcast
    e = events.Broadcast
    e.entry(c.ask_post)
    e.post(c.schedule)


def setup_signs():
    c = callbacks.signs
    e = events.Signs
    e.entry(c.menu)
    e.show(c.show)
    e.add(c.ask_new)
    e.new_text(c.save)
    e.delete(c.delete)


def setup_send_picture():
    c = callbacks.send_picture
    e = events.SendPicture
    e.command(c.send_link)
    e.start(c.start)
    e.recipient(c.ask_picture)
    e.send(c.send)
    c = callbacks.send_picture.on_picture_select
    e.select_cute_picture(c("cute"))
    e.select_angry_picture(c("angry"))
    c = callbacks.send_picture.on_picture_reselect
    e.reselect_cute_picture(c("cute"))
    e.reselect_angry_picture(c("angry"))


def setup_required_join():
    c = callbacks.required_join
    e = events.RequiredJoin
    e.entry(c.menu)
    e.add_channel(c.ask_post)
    e.channel_post(c.save)
    e.show(c.show)
    e.delete_channel(c.delete)
