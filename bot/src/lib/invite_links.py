from core import bot


async def get_chat_invite_link(chat_id: int) -> str:
    chat = await bot.get_chat(chat_id)

    if not chat.invite_link:
        chat.invite_link = await chat.create_invite_link()

    return chat.invite_link
