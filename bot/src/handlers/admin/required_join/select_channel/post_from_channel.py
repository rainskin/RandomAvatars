from aiogram.utils.exceptions import TelegramAPIError

import lib
from assets import States
from core import dp
from loader import api


@dp.any_message(state=States.required_join)
async def _(msg: lib.MESSAGE):
    from_channel = msg.forward_from_chat

    if not from_channel:
        await msg.answer('Ошибка, не вижу источник пересылки')
        return

    try:
        await lib.get_chat_invite_link(from_channel.id)
    except TelegramAPIError:
        await msg.answer('У меня нет нужных прав в этом канале')
        return

    await lib.reset_state()
    await api.required_join.set_chat_id(from_channel.id)
    await msg.answer('Обязательная подписка настроена')
