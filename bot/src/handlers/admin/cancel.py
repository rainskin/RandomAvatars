from aiogram import types
from aiogram.dispatcher import FSMContext

import lib.events.admin
from assets import kbs, texts


@lib.events.admin.back
async def _(query: types.CallbackQuery, state: FSMContext):
    await query.answer()
    await state.finish()
    await query.message.edit_text(texts.admin_panel, reply_markup=kbs.admin_panel)
