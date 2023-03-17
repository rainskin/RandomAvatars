from abc import ABC

from core import handlers
from lib.assets import PictureCategory, Texts
from lib.helpers import set_cooldown, save_chat, get_cooldown, get_picture, get_required_join


class PictureRequest(handlers.Handler, ABC):
    category: PictureCategory = None

    def set_category(self):
        raise NotImplementedError()

    async def post_reply(self):
        pass

    async def callback(self):
        await save_chat(self.chat)
        self.set_category()

        if not self.category:
            return

        await self._check_rights()
        await self._reply_picture()
        await self.post_reply()

    async def _check_rights(self):
        await self._check_cooldown()
        if self.is_chat_private:
            await self._check_required_join()

    async def _reply_picture(self):
        picture = await get_picture(self.category, self.chat)
        await self.reply_photos(picture)
        await set_cooldown(self.user)

    async def _check_cooldown(self):
        if not (cooldown := await get_cooldown(self.user, self.chat)):
            return

        text = Texts.wait.format(cooldown)
        await self.cancel(text)

    async def _check_required_join(self):
        if not (chat_id := await get_required_join()):
            return

        if await self.is_chat_member(chat_id):
            return

        link = await self.obtain_invite_link(chat_id)
        text = Texts.required_join.format(link)
        await self.cancel(text)
