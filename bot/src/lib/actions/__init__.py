from assets import keyboards, texts
from core import *
from .requests import on_text, respond_picture


async def send_main_menu(msg: MESSAGE):
    text = texts.welcome.format(mention=msg.from_user.get_mention())
    startgroup_url = await get_startgroup_link('0')
    kb = keyboards.MainMenu(startgroup_url)
    await utils.answer(msg, text, kb)
