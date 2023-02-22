from lib import *


@events.main_menu.get_picture
async def _(query: QUERY):
    if category := choose_picture_category(query):
        await on_picture_request(query, category)
