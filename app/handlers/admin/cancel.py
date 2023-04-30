from botty import dp, Query, FSMContext, e

import answers
from assets import kbs


@dp.button(kbs.BACK_BUTTON).state()
async def _(query: Query, state: FSMContext):
    await state.finish()
    await e(query, answers.ADMIN_MENU)
