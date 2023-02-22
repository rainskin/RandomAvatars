import lib


@lib.events.admin.select_channel
async def _(query: lib.QUERY):
    await lib.STATES.required_join.set()
    await lib.answers.ask_post_from_channel(query)
