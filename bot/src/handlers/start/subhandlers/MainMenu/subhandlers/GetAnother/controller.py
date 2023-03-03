from core import BaseController

from lib import on_picture_request, api


class Controller(BaseController):

    async def callback(self):
        category = await self.get_category()
        await on_picture_request(self.message, category)

    def get_category(self):
        user = api.user(self.message.from_user.id)
        return user.picture_category.get()
