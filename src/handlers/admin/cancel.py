from aiogram import types
from aiogram.dispatcher import FSMContext

from assets import kbs
from core import dp


@dp.click(kbs.Cancel.button, state='*')
async def _(query: types.CallbackQuery, state: FSMContext):
    await query.answer()
    await state.finish()
    await query.message.edit_text('Как скажешь..')
