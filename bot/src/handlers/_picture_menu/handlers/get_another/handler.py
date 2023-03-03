from core import BaseHandler

from lib import utils, respond_picture


class Handler(BaseHandler):

    async def callback(self):
        category = await utils.get_picture_category(self.message.from_user)
        await respond_picture(self.message, category)
