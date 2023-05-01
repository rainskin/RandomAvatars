from botty import dp, Query, r

import answers
from api import Sign, Text
from assets import kbs


@dp.button(kbs.AdminMenu.SIGNS)
async def entry(query: Query):
    await query.message.edit_reply_markup(kbs.SIGNS)


@dp.button(kbs.Signs.SHOW)
async def show(query: Query):
    if not (signs := Sign.find_all()):
        return await query.answer(Text.NO_SIGNS)
    for s in signs:
        await r(query, answers.sign(s))


@dp.button(kbs.SignMenu.DELETE)
def delete(query: Query, button: dict):
    Sign.remove(button["id"])
    return query.message.delete()
