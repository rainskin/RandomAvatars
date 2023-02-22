import lib


@lib.events.admin.required_join_disable
async def _(query: lib.QUERY):
    await query.answer()
    await lib.reset_required_join()
    await lib.answers.required_join_disabled(query)
