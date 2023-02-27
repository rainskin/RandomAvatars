from core.answers import answer_or_edit
from core.constants import *
from lib.assets import kbs
from lib.loader import api
from lib.utils import get_chat_invite_link


def disabled(query: QUERY):
    return answer_or_edit(query, 'Обязательная подписка отключена')


async def info(query: QUERY):
    required_chat_id = await api.required_join.get_chat_id()

    if required_chat_id:
        invite_link = await get_chat_invite_link(required_chat_id)
        text = f'Обязательная подписка: {invite_link}'
    else:
        text = f'Обязательная подписка отключена'

    await answer_or_edit(query, text, kbs.required_join)
