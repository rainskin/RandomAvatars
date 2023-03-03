from aiogram.dispatcher.filters.state import StatesGroup, State


class States(StatesGroup):
    broadcast = State()
    required_join = State()


STATES = States
