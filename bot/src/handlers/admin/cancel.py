import lib


@lib.events.admin.back
async def _(query: lib.QUERY):
    await query.answer()
    await lib.reset_state()
    await lib.answers.admin_panel(query)
