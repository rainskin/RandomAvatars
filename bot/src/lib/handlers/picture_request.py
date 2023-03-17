from core import handlers
from lib.api import api
from lib.assets import PictureCategory, Texts
from lib.helpers import save_chat, get_cooldown, get_picture, set_cooldown


class PictureRequest(handlers.Query):
    category: str = None

    async def callback(self):
        await save_chat(self.chat)
        category = self.category = self.pick_category()

        if category:
            await self.check_rights()
            await self.send()
            await self.on_success()

    async def check_rights(self):
        await self.check_required_join()
        await self.check_cooldown()

    async def check_cooldown(self):
        cooldown = await get_cooldown(self.user, self.chat)

        if not cooldown:
            return

        text = Texts.wait.format(cooldown)
        await self.cancel(text)

    async def check_required_join(self):
        chat_id = await self.get_required_chat_id()

        if not chat_id:
            return

        link = await self.obtain_invite_link(chat_id)
        text = Texts.required_join.format(link)
        await self.cancel(text)

    async def send(self):
        picture = await get_picture(self.category, self.chat)
        await self.reply_photos(picture)
        await set_cooldown(self.user)

    async def get_required_chat_id(self) -> int | None:
        if not self.is_chat_private:
            return None

        if not (chat_id := await api.required_join.get_chat_id()):
            return None

        if not await self.is_chat_member(chat_id):
            return chat_id

    def pick_category(self) -> PictureCategory | None:
        raise NotImplementedError()

    async def on_success(self):
        pass
