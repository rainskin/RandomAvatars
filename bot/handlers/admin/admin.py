from aiogram import types

import config
from assets import commands, kbs
from core import dp


@dp.command(commands.ADMIN, user_id=config.ADMIN_IDS)
async def _(msg: types.Message):
    await msg.answer('Вот твоя админ-панель, хозяин 🥵', reply_markup=kbs.admin_panel)
