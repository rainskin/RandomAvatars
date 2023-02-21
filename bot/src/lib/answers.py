from aiogram import types

from assets import texts


def does_not_work(msg: types.Message):
    return msg.answer(texts.command_not_work)
