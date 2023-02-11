from aiogram import types

from assets import commands, texts
from core import dp


@dp.command(commands.SEND_PICTURE)
async def _(msg: types.Message):
    await msg.answer(texts.command_not_work)
