from botty import dp, Query, e

import answers
from assets import kbs, BroadcastState


@dp.button(kbs.AdminMenu.BROADCAST)
async def _(query: Query):
    await BroadcastState.POST.set()
    await e(query, answers.ASK_POST)
