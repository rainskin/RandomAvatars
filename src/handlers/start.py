from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import ChatType

import lib
from assets import commands, texts
from core import dp


@dp.command(commands.START, state='*')
async def _(msg: types.Message, state: FSMContext):
    await state.finish()

    if msg.chat.type == ChatType.PRIVATE:
        await lib.answer_main_menu(msg)
    else:
        await msg.answer(texts.group_welcome)

    if lib.is_admin(msg.from_user):
        await commands.setup()
