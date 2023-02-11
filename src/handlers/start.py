from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.utils.deep_linking import get_startgroup_link

import lib
from assets import commands, texts, kbs
from core import dp


@dp.command(commands.START)
async def _(msg: types.Message, state: FSMContext):
    await state.finish()

    text = texts.welcome.format(mention=msg.from_user.get_mention())
    startgroup_url = await get_startgroup_link('0')
    kb = kbs.MainMenu(startgroup_url).create()
    await msg.answer(text, reply_markup=kb)

    if lib.is_admin(msg.from_user):
        await commands.setup()
