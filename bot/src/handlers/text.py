import lib


@lib.events.text
async def _(msg: lib.MESSAGE):
    if category := lib.choose_picture_category(msg):
        await lib.on_picture_request(msg, category)
