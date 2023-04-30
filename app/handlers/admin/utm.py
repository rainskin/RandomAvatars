from botty import dp, Query, e

import answers
from api import get_utm
from assets import kbs


@dp.button(kbs.AdminMenu.UTM)
def _(query: Query):
    utm = get_utm()
    return e(query, answers.utm(utm))
