from lib import *


@events.admin.required_join_disable
async def _(query: QUERY):
    await query.answer()
    await reset_required_join()
    await answers.required_join_disabled(query)
