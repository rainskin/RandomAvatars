from botty import FSMContext, Message, Query, TelegramAPIError, e, obtain_invite_link, r

from api import get_required_join_chat, reset_required_join, set_required_join_chat
from assets import RequiredJoinState, answers


async def menu(query: Query):
    invite_link = None
    if chat_id := get_required_join_chat():
        invite_link = await obtain_invite_link(chat_id)
    await e(query, answers.required_join(invite_link))


def disable(query: Query):
    reset_required_join()
    return e(query, answers.REQUIRED_JOIN)


async def ask_post(query: Query):
    await RequiredJoinState.post.set()
    await e(query, answers.ask_channel_post)


async def save(msg: Message, state: FSMContext):
    channel = msg.forward_from_chat
    if not channel:
        await r(msg, answers.forward_error)
        return
    try:
        invite_link = await obtain_invite_link(channel.id)
    except TelegramAPIError:
        await r(msg, answers.rights_error)
        return
    await state.finish()
    set_required_join_chat(channel.id)
    await r(msg, answers.required_join(invite_link))
