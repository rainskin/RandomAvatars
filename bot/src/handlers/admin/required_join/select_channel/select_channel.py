from lib import *


@events.admin.select_channel
async def _(query: QUERY):
    await STATES.required_join.set()
    await answers.ask_post_from_channel(query)
