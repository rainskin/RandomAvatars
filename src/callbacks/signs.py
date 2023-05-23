from botty import FSMContext, Message, Query, e, r

from api import Sign
from assets import SignState, answers, kbs, texts


async def menu(query: Query):
    await query.message.edit_reply_markup(kbs.signs)


async def show(query: Query):
    if not (signs := Sign.find_all()):
        await query.answer(texts.no_signs)
        return
    for s in signs:
        await r(query, answers.sign(s))


async def ask_new(query: Query):
    await SignState.sign.set()
    await e(query, answers.ask_sign)


async def save(msg: Message, state: FSMContext):
    await state.finish()
    Sign.add(msg.html_text)
    await r(msg, answers.signs)


async def delete(query: Query, button: dict[str, str]):
    Sign.remove(button["id"])
    await query.message.delete()
