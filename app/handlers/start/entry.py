from botty import dp, Message, FSMContext, r

import answers
from lib import save_chat


@dp.START
async def _(msg: Message, state: FSMContext):
    await state.finish()
    save_chat(msg)
    await r(msg, answers.start(msg))
