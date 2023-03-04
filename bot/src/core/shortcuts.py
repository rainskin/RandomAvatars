from aiogram import types

__all__ = [
    'UPDATE',
    'MESSAGE',
    'QUERY',
    'USER',
    'CHAT',
    'EVENT',
    'CHAT_TYPES',
]

UPDATE = types.Update
MESSAGE = types.Message
QUERY = types.CallbackQuery
USER = types.User
CHAT = types.Chat
EVENT = MESSAGE | QUERY
CHAT_TYPES = types.ChatType
