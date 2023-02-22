from lib import *


@events.admin.required_join
async def _(query: QUERY):
    await answers.required_join_info(query)
