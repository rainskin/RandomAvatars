from aiogram import types
from aiogram.dispatcher import FSMContext

from assets import kbs, texts
from core import dp


@dp.click(kbs.ADMIN_BACK_BUTTON, state='*')
async def _(query: types.CallbackQuery, state: FSMContext):
    await query.answer()
    await state.finish()
    await query.message.edit_text(texts.admin_panel, reply_markup=kbs.admin_panel)
