from botty import dp, e, Query

import answers
from api import reset_required_join
from assets import kbs


@dp.button(kbs.RequiredJoin.DISABLE)
def _(query: Query):
    reset_required_join()
    return e(query, answers.REQUIRED_JOIN)
