from lib import *


@events.admin.required_join_disable
async def _(query: QUERY):
    await query.answer()
    await utils.reset_required_join()
    await answers.required_join.disabled(query)
