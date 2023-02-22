from lib import *


@events.admin.broadcast
async def _(query: QUERY):
    await query.answer()
    await STATES.broadcast.set()
    await answers.ask_broadcast_post(query)
