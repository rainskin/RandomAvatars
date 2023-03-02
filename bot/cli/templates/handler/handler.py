from core import BaseHandler

from .assets import text, keyboard, state
from .lib import Scheduler


class Handler(BaseHandler):

    async def callback(self):
        await state.set()
        await self.answer(text, keyboard)
        self.schedule_answer()

    def schedule_answer(self):
        scheduler = Scheduler(self.message)
        scheduler.schedule_answer('Timer expired', delay=3)
