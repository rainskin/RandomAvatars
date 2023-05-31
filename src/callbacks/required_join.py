from botty import FSMContext, Message, Query, TelegramAPIError, e, obtain_invite_link, r

from api import RequiredJoin
from assets import RequiredJoinState, answers, texts


async def menu(query: Query):
    await e(query, answers.required_join)


async def delete(query: Query, button: dict[str, int]):
    RequiredJoin.remove(button["id"])
    await query.message.delete()


async def ask_post(query: Query):
    await RequiredJoinState.post.set()
    await e(query, answers.ask_channel_post)


async def save(msg: Message, state: FSMContext):
    channel = msg.forward_from_chat
    if not channel:
        await r(msg, answers.forward_error)
        return
    try:
        link = await obtain_invite_link(channel.id)
    except TelegramAPIError:
        await r(msg, answers.rights_error)
        return
    await state.finish()
    RequiredJoin.add(channel.id, link)
    await r(msg, answers.required_join)


async def show(query: Query):
    if not (join := RequiredJoin.find_all()):
        await query.answer(texts.no_required_join)
        return
    for j in join:
        await r(query, answers.required_join_chat(j.chat_id, j.link))
