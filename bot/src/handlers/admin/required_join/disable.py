from aiogram import types

from assets import kbs
from core import dp
from loader import api


@dp.click(kbs.RequiredJoin.disable)
async def _(query: types.CallbackQuery):
    await query.answer()
    await api.required_join.set_chat_id(None)
    await query.message.edit_text('Обязательная подписка отключена')
