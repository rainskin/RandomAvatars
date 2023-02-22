from lib import *


@events.admin.back
async def _(query: QUERY):
    await query.answer()
    await reset_state()
    await answers.admin_panel(query)
