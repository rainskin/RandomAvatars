from aiogram import types
from aiogram.dispatcher import FSMContext

from assets import commands, texts
from core import dp


@dp.command(commands.START)
async def _(msg: types.Message, state: FSMContext):
    await state.finish()
    await msg.answer(texts.welcome)
