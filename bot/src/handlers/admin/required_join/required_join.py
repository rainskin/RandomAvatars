import lib


@lib.events.admin.required_join
async def _(query: lib.QUERY):
    await lib.answers.required_join_info(query)
