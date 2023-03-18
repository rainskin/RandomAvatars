from telegram import Chat, User

from .api import api
from .assets import PictureCategory


async def save_chat(chat: Chat) -> None:
    await api.chats.save(chat.id)


async def get_cooldown(user: User, chat: Chat) -> int:
    return await api.user(user.id).cooldown.get(chat.type)


async def get_picture(category: str, chat: Chat) -> list[str]:
    return await api.pictures(category).get_random(chat.id)


async def set_cooldown(user: User) -> None:
    await api.user(user.id).cooldown.set()


async def get_required_join() -> int:
    return await api.required_join.get_chat_id()


async def save_picture_category(user: User, category: PictureCategory) -> None:
    await api.user(user.id).picture_category.set(category)


async def get_picture_category(user: User) -> PictureCategory:
    result = await api.user(user.id).picture_category.get()
    return PictureCategory(result)
