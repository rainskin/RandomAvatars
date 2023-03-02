from lib import *
from .assets import event


class Handler(BaseHandler):
    async def callback(self):
        category = await utils.get_picture_category(self.message.from_user)

        if not category:
            return await answers.ask_to_restart_bot(self.message)

        await answers.requests.respond_picture(self.message, category)


Handler.setup(event)
