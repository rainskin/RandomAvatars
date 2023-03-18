from core import *
from handlers.Admin import assets as admin
from .. import assets as broadcast


class Keyboard(InlineKeyboard):
    confirm = CallbackButton('Запускай!')

    def __init__(self):
        self.add_rows(
            self.confirm,
            admin.BACK_BUTTON,
        )


class Storage(BaseStorage):
    class _Keys:
        POST_ID = 'post_id'

    async def get_post_id(self) -> int:
        return await self.get(self._Keys.POST_ID)

    async def set_post_id(self, value: int):
        await self.set(self._Keys.POST_ID, value)


event = dp.any_message(state=broadcast.post_state)
text = 'Начать рассылку?'
keyboard = Keyboard()
confirm_state = State(__name__)
