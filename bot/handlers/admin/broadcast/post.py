from aiogram import types
from aiogram.dispatcher import FSMContext

import lib
from assets import States
from core import dp


@dp.any_message(state=States.broadcast)
async def _(msg: types.Message, state: FSMContext):
    await state.finish()
    await msg.answer('Начинаю рассылку..')
    lib.schedule_broadcast(msg)
