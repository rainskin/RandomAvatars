from core import handlers
from lib.api import api
from lib.assets import PictureCategory
from lib.MainMenu.assets import Texts


class PictureRequest(handlers.Query):
    category: str = None

    async def callback(self):
        category = self.category = self.pick_category()
        if category:
            await self.respond()
            await self.on_success()

    def pick_category(self) -> PictureCategory | None:
        raise NotImplementedError()

    async def on_success(self):
        pass

    async def respond(self):
        await api.chats.save(self.chat.id)

        if chat_id := await self.get_chat_id():
            link = await self.obtain_invite_link(chat_id)
            text = Texts.required_join.format(link)
            await self.cancel(text)  # TODO: test

        if cooldown := await api.user(self.user.id).cooldown.get(self.chat.type):
            text = Texts.wait.format(cooldown)
            await self.cancel(text)

        picture = await api.pictures(self.category).get_random(self.chat.id)
        await self.send(picture)

    async def send(self, picture: list[str]):
        await self.reply_photos(picture)
        await api.user(self.user.id).cooldown.set()

    async def get_chat_id(self) -> int | None:
        if self.chat.type != self.chat.PRIVATE:
            return None

        if not (chat_id := await api.required_join.get_chat_id()):
            return None

        if not await self.is_chat_member(chat_id):
            return chat_id
