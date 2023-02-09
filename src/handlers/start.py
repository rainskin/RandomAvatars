from aiogram import types
from aiogram.dispatcher import FSMContext

import lib
from assets import commands, texts
from core import dp


@dp.command(commands.START)
async def _(msg: types.Message, state: FSMContext):
    await state.finish()

    text = texts.welcome.format(mention=msg.from_user.get_mention())
    await msg.answer(text)

    if lib.is_admin(msg.from_user):
        await commands.setup()
