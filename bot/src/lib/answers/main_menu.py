from aiogram.utils.deep_linking import get_startgroup_link

from core.answers import answer
from lib.assets import texts, kbs
from core.constants import *


async def send(msg: MESSAGE):
    text = texts.welcome.format(mention=msg.from_user.get_mention())
    startgroup_url = await get_startgroup_link('0')
    kb = kbs.MainMenu(startgroup_url)
    await answer(msg, text, kb)
