from botty import FSMContext, Message, Query, e, r

from api import get_utm
from assets import answers


def menu(msg: Message):
    return r(msg, answers.admin_menu)


def send_utm(query: Query):
    utm = get_utm()
    return e(query, answers.utm(utm))


async def back(query: Query, state: FSMContext):
    await state.finish()
    await e(query, answers.admin_menu)
