import lib


@lib.events.admin.broadcast
async def _(query: lib.QUERY):
    await query.answer()
    await lib.STATES.broadcast.set()
    await lib.answers.ask_broadcast_post(query)
