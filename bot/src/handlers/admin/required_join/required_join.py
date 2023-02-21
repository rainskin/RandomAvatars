import lib
from assets import kbs
from core import dp
from loader import api


@dp.click(kbs.AdminPanel.required_join)
async def _(query: lib.QUERY):
    required_chat_id = await api.required_join.get_chat_id()

    if required_chat_id:
        invite_link = await lib.get_chat_invite_link(required_chat_id)
        text = f'Обязательная подписка: {invite_link}'
    else:
        text = f'Обязательная подписка отключена'

    await query.message.edit_text(text, reply_markup=kbs.required_join)
