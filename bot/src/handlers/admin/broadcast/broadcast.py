from aiogram import types

from assets import kbs, texts, States
from core import dp


@dp.click(kbs.AdminPanel.broadcast)
async def _(query: types.CallbackQuery):
    await query.answer()
    await States.broadcast.set()
    await query.message.edit_text(texts.ask_broadcast_post, reply_markup=kbs.admin_cancel)
