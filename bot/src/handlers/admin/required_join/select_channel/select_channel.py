from aiogram import types

from assets import kbs, texts, States
from core import dp


@dp.click(kbs.RequiredJoin.select_channel)
async def _(query: types.CallbackQuery):
    await States.required_join.set()
    await query.message.edit_text(texts.ask_post_from_channel, reply_markup=kbs.admin_cancel)
