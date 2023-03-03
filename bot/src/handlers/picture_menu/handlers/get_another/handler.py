from core import BaseHandler

from lib import respond_picture, api


class Handler(BaseHandler):

    async def callback(self):
        category = await self.get_category()
        await respond_picture(self.message, category)

    def get_category(self):
        user = api.user(self.message.from_user.id)
        return user.picture_category.get()
