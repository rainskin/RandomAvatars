import config
from assets import commands
from core import *
from .assets import welcome_text, Keyboard


async def update_my_commands():
    await bot.set_my_commands(commands.Groups.for_users)

    for admin_id in config.ADMIN_IDS:
        with suppress(TelegramAPIError):
            scope = BotCommandScopeChat(admin_id)
            await bot.set_my_commands(commands.Groups.for_admins, scope)


async def send_main_menu(msg: MESSAGE):
    text = welcome_text.format(mention=msg.from_user.get_mention())
    startgroup_url = await get_startgroup_link('0')
    kb = Keyboard(startgroup_url)
    await utils.answer(msg, text, kb)
