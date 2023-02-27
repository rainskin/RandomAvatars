from lib import *


@events.main_menu.get_picture
async def _(query: QUERY):
    await answers.requests.respond(query)
