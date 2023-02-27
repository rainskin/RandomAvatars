from aiogram import types

__all__ = [
    'UPDATE',
    'MESSAGE',
    'QUERY',
    'USER',
    'CHAT',
    'REQUEST',
]

UPDATE = types.Update
MESSAGE = types.Message
QUERY = types.CallbackQuery
USER = types.User
CHAT = types.Chat
REQUEST = MESSAGE | QUERY
