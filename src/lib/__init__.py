from aiogram import types

from assets import PictureCategory


async def answer_random_picture(msg: types.Message, category: PictureCategory):
    await msg.answer_photo('https://photovords.ru/pics_max/photowords_ru_6809.jpg')
