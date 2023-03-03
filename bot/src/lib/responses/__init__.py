from aiogram.utils.deep_linking import get_startgroup_link
from core.answers import answer
from core.constants import *

from assets import keyboards, texts
from .requests import on_any_request, respond_picture


async def send_main_menu(msg: MESSAGE):
    text = texts.welcome.format(mention=msg.from_user.get_mention())
    startgroup_url = await get_startgroup_link('0')
    kb = keyboards.MainMenu(startgroup_url)
    await answer(msg, text, kb)
