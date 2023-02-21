from aiogram import types

from assets import States

__all__ = [
    'UPDATE',
    'MESSAGE',
    'QUERY',
    'REQUEST',
    'USER',
    'CHAT',
    'STATES',
]

UPDATE = types.Update
MESSAGE = types.Message
QUERY = types.CallbackQuery
REQUEST = MESSAGE | QUERY
USER = types.User
CHAT = types.Chat

STATES = States
