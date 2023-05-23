from contextlib import suppress

from botty import FSMContext, Message, NoSendTextRights, Update, r

from assets import PictureCategory, answers
from lib import on_picture_request, pick_category, save_chat

from . import admin, broadcast, menu, required_join, send_picture, signs

__all__ = ("signs", "required_join", "send_picture", "broadcast", "menu", "admin")


async def start(msg: Message, state: FSMContext):
    await state.finish()
    save_chat(msg)
    await r(msg, answers.start(msg))


def get_command(category: PictureCategory):
    def callback(msg: Message):
        return on_picture_request(msg, category)

    return callback


async def ask_rights(upd: Update, _: Exception):
    if not (event := upd.message or upd.callback_query):
        return False
    with suppress(NoSendTextRights):
        await r(event, answers.ask_rights)
    return True


async def check_triggers(msg: Message):
    if category := pick_category(msg.text):
        await on_picture_request(msg, category)
