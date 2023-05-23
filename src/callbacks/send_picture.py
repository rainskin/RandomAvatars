from typing import cast

from botty import FSMContext, Message, Query, bot, is_private

from assets import PictureCategory, buttons, texts
from assets import SendPictureState as State
from assets import answers as a
from deps import e, r
from lib import PictureRequest, save_chat


async def start(msg: Message, state: FSMContext):
    save_chat(msg)
    args = msg.get_args() or ""
    group_id = int(args.removeprefix(buttons.GROUP_PREFIX))
    await State.recipient.set()
    await state.update_data(group_id=group_id)  # type: ignore[TODO]
    await r(msg, a.ask_picture_recipient)


def send_link(msg: Message):
    if is_private(msg.chat):
        return r(msg, a.only_for_groups)
    return r(msg, a.send_picture_info(msg.chat.id))


async def ask_picture(msg: Message, state: FSMContext):
    await State.picture.set()
    await state.update_data(recipient=msg.text)  # type: ignore[TODO]
    await r(msg, a.select_picture)


def on_picture_select(category: PictureCategory):
    async def callback(query: Query):
        request = PictureRequest(query.from_user, query.message)
        picture = await request.fetch_picture(category)
        if not picture:
            return
        await State.confirm.set()
        await r(query, a.reselect_picture(picture[0]))

    return callback


def on_picture_reselect(category: PictureCategory):
    async def callback(query: Query):
        request = PictureRequest(query.from_user, query.message)
        picture = await request.fetch_picture(category)
        if not picture:
            return
        await e(query, a.reselect_picture(picture[0]))

    return callback


async def send(query: Query, state: FSMContext):
    photo = query.message.photo[-1].file_id
    session = await state.get_data()  # type: ignore[TODO]
    group_id = cast(int, session["group_id"])
    recipient = cast(str, session["recipient"])
    text = texts.picture_for(recipient, query.from_user.get_mention())
    await state.finish()
    sent_msg = await bot.send_photo(group_id, photo, text)
    if sent_msg.chat.type == "group":
        url = sent_msg.chat.username or f'"{sent_msg.chat.title}"'
    else:
        url = sent_msg.url
    await r(query, a.picture_sent(url))
