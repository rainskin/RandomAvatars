import aiogram
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State
from aiogram.utils import executor

from .bot import Bot, bot
from .keyboards import CallbackButton


class Dispatcher(aiogram.Dispatcher):
    def __init__(self, _bot: Bot):
        super().__init__(_bot, storage=MemoryStorage())

    def command(self, value: str | list[str], user_id: list[int] = None, state: State | str = None):
        return self.message_handler(commands=value, user_id=user_id, state=state)

    def any_message(self, state: State | str = None):
        return self.message_handler(content_types='any', state=state)

    def click(
            self,
            button: str | CallbackButton | list[CallbackButton],
            state: State | str = None,
    ):
        if isinstance(button, str):
            return self.message_handler(text=button, state=state)

        if isinstance(button, CallbackButton):
            text = button.data
        else:
            text = [i.data for i in button]

        return self.callback_query_handler(text=text, state=state)

    def text(self, value: str = None):
        return self.message_handler(text=value)

    def run(self, skip_updates: bool):
        executor.start_polling(self, skip_updates=skip_updates)


dp = Dispatcher(bot)
