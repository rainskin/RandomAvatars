from core import handlers
from lib.assets import PictureCategory, Texts
from lib.helpers import *


class PictureRequest(handlers.Query):
    category: PictureCategory = None

    def pick_category(self) -> PictureCategory | None:
        raise NotImplementedError()

    async def on_success(self):
        pass

    async def callback(self):
        await save_chat(self.chat)
        self.category = self.pick_category()

        if not self.category:
            return

        await self._check_rights()
        await self._reply_picture()
        await self.on_success()

    async def _check_rights(self):
        await self.check_cooldown()
        if self.is_chat_private:
            await self.check_required_join()

    async def _reply_picture(self):
        picture = await get_picture(self.category, self.chat)
        await self.reply_photos(picture)
        await set_cooldown(self.user)

    async def check_cooldown(self):
        cooldown = await get_cooldown(self.user, self.chat)

        if not cooldown:
            return

        text = Texts.wait.format(cooldown)
        await self.cancel(text)

    async def check_required_join(self):
        chat_id = await get_required_join()

        if not chat_id:
            return

        if await self.is_chat_member(chat_id):
            return

        link = await self.obtain_invite_link(chat_id)
        text = Texts.required_join.format(link)
        await self.cancel(text)
