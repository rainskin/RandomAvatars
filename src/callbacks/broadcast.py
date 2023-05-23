from botty import FSMContext, Message, Query, e, r, schedule_broadcast

from api import get_chats
from assets import BroadcastState, answers


async def ask_post(query: Query):
    await BroadcastState.post.set()
    await e(query, answers.ask_post)


async def schedule(msg: Message, state: FSMContext):
    await state.finish()
    await r(msg, answers.broadcast_start)
    schedule_broadcast(msg, get_chats())
