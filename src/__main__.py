from aiogram import executor

import handlers
from core import dp

handlers.setup()
executor.start_polling(dp, skip_updates=True)
