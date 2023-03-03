from core import utils
from lib import api


async def get_text():
    chat_id = await api.required_join.get_chat_id()

    if not chat_id:
        return 'Обязательная подписка отключена'

    invite_link = await utils.get_invite_link(chat_id)
    return f'Обязательная подписка: {invite_link}'
