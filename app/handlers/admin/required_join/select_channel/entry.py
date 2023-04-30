from botty import dp, e, Query

import answers
from assets import kbs, RequiredJoinState as State


@dp.button(kbs.RequiredJoin.SELECT_CHANNEL)
async def _(query: Query):
    await State.POST.set()
    await e(query, answers.ASK_CHANNEL_POST)
