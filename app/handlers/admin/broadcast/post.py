from botty import dp, Message, FSMContext, r, schedule_broadcast

import answers
from api import get_chats
from assets import BroadcastState


@dp.MESSAGE.state(BroadcastState.POST)
async def _(msg: Message, state: FSMContext):
    await state.finish()
    await r(msg, answers.BROADCAST_START)
    schedule_broadcast(msg, get_chats())
