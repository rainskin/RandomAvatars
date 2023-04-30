from botty import dp, obtain_invite_link, Query, e

import answers
from api import get_required_join_chat
from assets import kbs


@dp.button(kbs.AdminMenu.REQUIRED_JOIN)
async def _(query: Query):
    invite_link = None
    if chat_id := get_required_join_chat():
        invite_link = await obtain_invite_link(chat_id)
    await e(query, answers.required_join(invite_link))
