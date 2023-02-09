from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State

import config
from src import kb, text

bot = Bot(token=config.TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())


class States(StatesGroup):
    add_content = State()
    choosing_amount = State()


@dp.message_handler(commands='start', state='*')
async def cmd_start(msg: types.Message, state: FSMContext):
    await state.finish()
    await msg.answer(text.start)


@dp.message_handler(commands='admin', state='*')
async def cmd_start(msg: types.Message, state: FSMContext):
    await msg.answer(text.admin, reply_markup=kb.admin)


@dp.callback_query_handler(text='upload')
async def upload(callback_query: types.CallbackQuery):
    await bot.send_message(callback_query.message.chat.id, text.upload, reply_markup=kb.content_category_kb)


@dp.callback_query_handler()
async def chose_category(callback_query: types.CallbackQuery, state: FSMContext):
    category = callback_query.data
    if category == 'single_avatars':
        await bot.send_message(callback_query.message.chat.id, 'Авы')
    elif category == 'paired_avatars':
        await bot.send_message(callback_query.message.chat.id, 'Парные авы')
    else:
        await bot.send_message(callback_query.message.chat.id, 'Пока не знаю что сказать')

    await States.add_content.set()
    await state.update_data(category=category)
    await bot.send_message(callback_query.message.chat.id, 'Отправь пикчи для загрузки и нажми ГОТОВО',
                           reply_markup=kb.done_kb)


@dp.message_handler(state=States.add_content, content_types=['photo'])
async def upload(msg: types.Message, state: FSMContext):
    if msg.text is None:
        photo_id = msg.photo[-1].file_id
        data = await state.get_data()
        images = data.get("images", [])
        category = data['category']
        await state.update_data(images=images + [photo_id])

        item = {
            'tg_id': photo_id
        }
        print(images)
        # loader.single_avatars.insert_one(item)


@dp.message_handler(state=States.add_content, content_types=['text'])
async def finish_upload(msg: types.Message, state: FSMContext):
    data = await state.get_data('images')

    if msg.text == 'Готово':
        if 'images' in data:
            count = len(data['images'])
            await bot.send_message(chat_id=msg.chat.id, text=f'Добавил {count} картинок', reply_markup=kb.remove)
            await state.finish()
        else:
            await bot.send_message(chat_id=msg.chat.id, text='Сначала загрузи фото')
    else:
        await bot.send_message(chat_id=msg.chat.id, text=f'Нажми ГОТОВО')


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
