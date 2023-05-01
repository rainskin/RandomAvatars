from botty import dp, Message, FSMContext, r, e, Query

import answers
from api import Sign
from assets import SignState as State, kbs


@dp.button(kbs.Signs.ADD)
async def entry(query: Query):
    await State.SIGN.set()
    await e(query, answers.ASK_SIGN)


@dp.TEXT.state(State.SIGN)
async def sign(msg: Message, state: FSMContext):
    await state.finish()
    Sign.add(msg.html_text)
    await r(msg, answers.SIGNS)
