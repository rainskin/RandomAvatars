from botty import dp, r, Message, obtain_invite_link, TelegramAPIError, FSMContext

import answers
from api import set_required_join_chat
from assets import RequiredJoinState as State


@dp.MESSAGE.state(State.POST)
async def _(msg: Message, state: FSMContext):
    channel = msg.forward_from_chat
    if not channel:
        return await r(msg, answers.FORWARD_ERROR)
    try:
        invite_link = await obtain_invite_link(channel.id)
    except TelegramAPIError:
        return await r(msg, answers.RIGHTS_ERROR)
    await state.finish()
    set_required_join_chat(channel.id)
    await r(msg, answers.required_join(invite_link))
